from rest_framework.views import APIView
from rest_framework.response import Response
from .agent import JarvisAgent

class JarvisInteractionView(APIView):
    def post(self, request):
        agent = JarvisAgent()
        command = request.data.get("command", "")
        # Ici on pourrait intégrer la logique pour interagir avec Expert + ML
        response_text = f"Jarvis a reçu votre commande: {command}"
        agent.tts.speak(response_text)
        return Response({"response": response_text})
