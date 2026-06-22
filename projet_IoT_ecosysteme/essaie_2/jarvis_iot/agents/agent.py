from .stt_engine import STTEngine
from .tts_engine import TTSEngine

class JarvisAgent:
    def __init__(self):
        self.stt = STTEngine()
        self.tts = TTSEngine()

    def listen_and_respond(self, response_text):
        user_command = self.stt.listen()
        print(f"Utilisateur: {user_command}")
        self.tts.speak(response_text)
