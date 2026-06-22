from django.urls import path
from .views import JarvisInteractionView

urlpatterns = [
    path('interact/', JarvisInteractionView.as_view(), name='jarvis_interact'),
]
