from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenue dans Jarvis IoT</h1><p>Votre backend fonctionne ✅</p>")
