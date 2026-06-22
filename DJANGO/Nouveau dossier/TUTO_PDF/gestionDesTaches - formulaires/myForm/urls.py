from django.urls import path
from . import views

app_name = "myForm"

urlpatterns  = [
    path('', views.contact ,name="contact"),
    path("/<cid>/" , views.detail , name ="detail")    
]