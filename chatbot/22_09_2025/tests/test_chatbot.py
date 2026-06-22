from types import SimpleNamespace
import sys
from pathlib import Path
from unittest import TestCase

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from core.chatbot import PDFChatBot


class FakeEmbeddings:
    def encode(self, texts):
        return [[0.1, 0.2, 0.3] for _ in texts]


class FakeVectorStore:
    def query(self, query_embeddings, n_results):
        return {"documents": [["contexte important du PDF"]]}


class FakeCompletions:
    def __init__(self):
        self.last_messages = None

    def create(self, model, messages, temperature):
        self.last_messages = messages
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(content="reponse basee sur le contexte")
                )
            ]
        )


class FakeClient:
    def __init__(self):
        self.completions = FakeCompletions()
        self.chat = SimpleNamespace(completions=self.completions)


class PDFChatBotTests(TestCase):
    def test_uses_pdf_context_when_vector_store_is_available(self):
        client = FakeClient()
        bot = PDFChatBot(
            vector_store=FakeVectorStore(),
            embedding_model=FakeEmbeddings(),
            openai_client=client,
            provider="openai",
        )

        response = bot.ask_question("Que dit le PDF ?")

        self.assertEqual(response["answer"], "reponse basee sur le contexte")
        self.assertEqual(response["sources"], ["contexte important du PDF"])
        self.assertIn("CONTEXTE DU PDF", client.completions.last_messages[1]["content"])

    def test_returns_clear_error_without_openai_client(self):
        bot = PDFChatBot(openai_client=None, provider="openai")

        response = bot.ask_question("Bonjour")

        self.assertIn("error", response)
        self.assertIn("OPENAI_API_KEY", response["error"])

    def test_local_mode_answers_from_pdf_context_without_openai(self):
        bot = PDFChatBot(
            vector_store=FakeVectorStore(),
            embedding_model=FakeEmbeddings(),
            openai_client=None,
            provider="local",
        )

        response = bot.ask_question("Que dit le PDF ?")

        self.assertNotIn("error", response)
        self.assertIn("Mode local actif", response["answer"])
        self.assertEqual(response["sources"], ["contexte important du PDF"])
