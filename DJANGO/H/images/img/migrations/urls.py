from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path("projects/", views.project_listing , name= "project"),
    path('<slug:id>/', views.project_detail, name="project_detail"),
    path("project/new", views.create_project),
]


