import os
import sys
from pathlib import Path

import streamlit as st


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import settings
from core.chatbot import PDFChatBot
from core.pdf_processor import PDFProcessor
from core.vector_store import VectorStoreManager


class ChatBotApp:
    def __init__(self):
        self.setup_page()

    def setup_page(self):
        st.set_page_config(
            page_title="Chatbot PDF Intelligent",
            page_icon=":page_facing_up:",
            layout="wide",
        )
        st.title("Chatbot PDF Intelligent")
        st.caption("Posez une question librement, ou ajoutez un PDF pour limiter les reponses au document.")

    def run(self):
        self._ensure_session_state()

        with st.sidebar:
            st.header("Configuration")
            self._render_ai_status()
            audio_enabled = False
            if settings.LLM_PROVIDER == "openai":
                audio_enabled = st.checkbox("Audio OpenAI", value=False)
            st.divider()
            st.header("PDF")
            uploaded_file = st.file_uploader(
                "Choisissez un fichier PDF",
                type="pdf",
                help="Le PDF reste local au serveur de l'application.",
            )

        if uploaded_file is not None:
            self._load_pdf_if_needed(uploaded_file)

        self._render_history()
        self._handle_prompt(audio_enabled)

    def _ensure_session_state(self):
        if "chatbot" not in st.session_state:
            st.session_state.chatbot = PDFChatBot()
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "uploaded_pdf_id" not in st.session_state:
            st.session_state.uploaded_pdf_id = None

    def _render_ai_status(self):
        if settings.LLM_PROVIDER == "local":
            st.info("Mode local actif")
        elif settings.OPENAI_API_KEY:
            st.success("OpenAI configure")
        else:
            st.warning("OPENAI_API_KEY absent")

    def _load_pdf_if_needed(self, uploaded_file):
        upload_id = f"{uploaded_file.name}:{uploaded_file.size}"
        if st.session_state.uploaded_pdf_id == upload_id:
            return

        temp_path = self._save_upload(uploaded_file)
        with st.spinner("Extraction du texte..."):
            text = PDFProcessor().extract_text(str(temp_path))

        with st.spinner("Creation de la base de connaissances..."):
            vector_store = VectorStoreManager().create_from_text(text)
            st.session_state.chatbot = PDFChatBot(vector_store=vector_store)

        st.session_state.uploaded_pdf_id = upload_id
        st.session_state.messages = []
        st.success("PDF pret.")

    def _save_upload(self, uploaded_file) -> Path:
        temp_dir = Path(settings.TEMP_DIR)
        temp_dir.mkdir(parents=True, exist_ok=True)
        safe_name = Path(uploaded_file.name).name
        temp_path = temp_dir / safe_name
        with open(temp_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        return temp_path

    def _render_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def _handle_prompt(self, audio_enabled: bool):
        prompt = st.chat_input("Posez votre question...")
        if not prompt:
            return

        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Recherche..."):
                response = st.session_state.chatbot.ask_question(prompt)

            if "error" in response:
                st.error(response["error"])
                answer = "Erreur"
            else:
                answer = response["answer"]
                st.markdown(answer)
                self._render_audio(answer, audio_enabled)
                self._render_sources(response.get("sources", []))

        st.session_state.messages.append({"role": "assistant", "content": answer})

    def _render_audio(self, answer: str, audio_enabled: bool):
        if not audio_enabled:
            return

        audio_path = st.session_state.chatbot.synthesize_speech(answer)
        if audio_path:
            st.audio(audio_path, format="audio/mp3")

    def _render_sources(self, sources: list[str]):
        if not sources:
            return

        with st.expander("Sources utilisees"):
            for index, document in enumerate(sources, start=1):
                st.write(f"Source {index}: {document[:300]}...")


if __name__ == "__main__":
    app = ChatBotApp()
    app.run()
