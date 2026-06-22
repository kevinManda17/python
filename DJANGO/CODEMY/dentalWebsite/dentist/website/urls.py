from django.urls import path
from . import views 


urlpatterns = [
    path("", views.index , name="home"),
    path("contact.html", views.contact , name="contact"),
    
]