from django.urls import path 
from . import views

urlpatterns =[
    path('myHome',views.myHome, name='myHome'),
]