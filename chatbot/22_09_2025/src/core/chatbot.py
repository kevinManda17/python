from pathlib import Path
import re
from typing import Any, Optional

from sentence_transformers import SentenceTransformer

from config.settings import settings


_CLIENT_SENTINEL = object()


class PDFChatBot:
    def __init__(
        self,
        vector_store: Optional[Any] = None,
        embedding_model: Optional[Any] = None,
        openai_client: Any = _CLIENT_SENTINEL,
        provider: Optional[str] = None,
    ):
        self.vector_store = vector_store
        self._embedding_model = embedding_model
        self._openai_error: Optional[str] = None
        self.provider = self._normalize_provider(provider or settings.LLM_PROVIDER)

        if self.provider == "openai" and openai_client is _CLIENT_SENTINEL:
            self.client = self._build_openai_client()
        elif openai_client is not _CLIENT_SENTINEL:
            self.client = openai_client
        else:
            self.client = None

    @property
    def embeddings(self):
        if self._embedding_model is None:
            self._embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)
        return self._embedding_model

    def ask_question(self, question: str) -> dict:
        question = (question or "").strip()
        if not question:
            return {"error": "Pose une question avant de lancer la recherche."}

        contexts = self._find_relevant_contexts(question)
        if self.vector_store is not None and self._openai_error:
            return {"error": self._openai_error}

        if self.provider == "local":
            return self._answer_locally(question, contexts)

        if self.client is None:
            return {
                "error": (
                    self._openai_error
                    or "Cle API OpenAI non configuree. Ajoute OPENAI_API_KEY dans .env "
                    "ou dans les secrets de la plateforme d'hebergement."
                )
            }

        messages = self._build_messages(question, contexts)

        try:
            completion = self.client.chat.completions.create(
                model=settings.LLM_MODEL,
                messages=messages,
                temperature=settings.TEMPERATURE,
            )
            answer = completion.choices[0].message.content or ""
            return {"answer": answer.strip(), "sources": contexts}
        except Exception as exc:
            return {"error": f"Erreur OpenAI: {exc}"}

    def synthesize_speech(self, text: str, output_path: str = "data/temp/response.mp3"):
        if self.provider != "openai" or self.client is None or not text:
            return None

        try:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            response = self.client.audio.speech.create(
                model=settings.TTS_MODEL,
                voice=settings.TTS_VOICE,
                input=text,
            )
            if hasattr(response, "write_to_file"):
                response.write_to_file(str(path))
            else:
                with open(path, "wb") as audio_file:
                    audio_file.write(response.content)
            return str(path)
        except Exception:
            return None

    def _build_openai_client(self):
        if self.provider != "openai":
            return None

        if not settings.OPENAI_API_KEY:
            return None

        try:
            from openai import OpenAI
        except ImportError:
            self._openai_error = (
                "Le package openai n'est pas installe. Lance: pip install -r requirements.txt"
            )
            return None

        return OpenAI(api_key=settings.OPENAI_API_KEY)

    def _answer_locally(self, question: str, contexts: list[str]) -> dict:
        if not contexts:
            return {
                "answer": (
                    "Mode local actif. Je peux repondre a partir d'un PDF charge, "
                    "mais je n'ai pas trouve de contexte dans un document pour cette question."
                ),
                "sources": [],
            }

        sentences = self._rank_context_sentences(question, contexts)
        if not sentences:
            preview = contexts[0].strip()[:800]
            return {
                "answer": f"Mode local actif. Passage le plus pertinent trouve:\n\n{preview}",
                "sources": contexts,
            }

        answer = "Mode local actif. D'apres le PDF:\n\n" + "\n".join(
            f"- {sentence}" for sentence in sentences[:4]
        )
        return {"answer": answer, "sources": contexts}

    def _find_relevant_contexts(self, question: str) -> list[str]:
        if self.vector_store is None:
            return []

        try:
            question_embedding = self.embeddings.encode([question])
            if hasattr(question_embedding, "tolist"):
                question_embedding = question_embedding.tolist()
            results = self.vector_store.query(
                query_embeddings=question_embedding,
                n_results=settings.RETRIEVAL_TOP_K,
            )
            documents = results.get("documents", [])
            if documents and isinstance(documents[0], list):
                return [doc for doc in documents[0] if doc]
            return [doc for doc in documents if doc]
        except Exception as exc:
            self._openai_error = f"Erreur de recherche dans le PDF: {exc}"
            return []

    def _build_messages(self, question: str, contexts: list[str]) -> list[dict[str, str]]:
        if contexts:
            context_text = "\n\n---\n\n".join(contexts)
            user_prompt = (
                "CONTEXTE DU PDF:\n"
                f"{context_text}\n\n"
                "QUESTION:\n"
                f"{question}"
            )
            system_prompt = (
                "Tu es un assistant pedagogique francophone. Reponds uniquement avec "
                "les informations presentes dans le contexte du PDF. Si la reponse "
                "n'est pas dans le contexte, dis clairement que tu ne sais pas."
            )
        else:
            user_prompt = question
            system_prompt = (
                "Tu es un assistant pedagogique francophone. Reponds clairement, "
                "simplement et de facon utile."
            )

        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def _rank_context_sentences(self, question: str, contexts: list[str]) -> list[str]:
        question_terms = self._keywords(question)
        scored = []

        for context_index, context in enumerate(contexts):
            for sentence in self._split_sentences(context):
                terms = self._keywords(sentence)
                if not terms:
                    continue
                overlap = len(question_terms.intersection(terms))
                score = overlap * 10 + max(0, 3 - context_index)
                if overlap or context_index == 0:
                    scored.append((score, len(sentence), sentence))

        scored.sort(key=lambda item: (-item[0], item[1]))
        unique = []
        seen = set()
        for _, _, sentence in scored:
            normalized = " ".join(sentence.lower().split())
            if normalized in seen:
                continue
            seen.add(normalized)
            unique.append(sentence)
        return unique

    def _split_sentences(self, text: str) -> list[str]:
        text = re.sub(r"\s+", " ", text or "").strip()
        parts = re.split(r"(?<=[.!?;:])\s+|\n+", text)
        return [part.strip() for part in parts if 40 <= len(part.strip()) <= 500]

    def _keywords(self, text: str) -> set[str]:
        stopwords = {
            "avec",
            "cest",
            "dans",
            "des",
            "est",
            "les",
            "pour",
            "que",
            "quoi",
            "qui",
            "sur",
            "une",
            "un",
        }
        words = re.findall(r"[a-zA-Z0-9]+", (text or "").lower())
        return {word for word in words if len(word) > 2 and word not in stopwords}

    def _normalize_provider(self, provider: str) -> str:
        provider = (provider or "local").strip().lower()
        if provider not in {"local", "openai"}:
            return "local"
        return provider
