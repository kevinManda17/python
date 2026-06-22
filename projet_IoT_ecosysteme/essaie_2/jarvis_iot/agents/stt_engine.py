import speech_recognition as sr

class STTEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Jarvis écoute...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='fr-FR')
                return text
            except sr.UnknownValueError:
                return ""
