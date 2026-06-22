from pathlib import Path

from config.settings import settings


class TextToSpeech:
    def __init__(self):
        self.client = self._build_client()

    def synthesize(self, text: str, output_path: str = "data/temp/response.mp3"):
        if self.client is None or not text:
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
                with open(path, "wb") as file:
                    file.write(response.content)
            return str(path)
        except Exception:
            return None

    def _build_client(self):
        if not settings.OPENAI_API_KEY:
            return None

        try:
            from openai import OpenAI
        except ImportError:
            return None

        return OpenAI(api_key=settings.OPENAI_API_KEY)
