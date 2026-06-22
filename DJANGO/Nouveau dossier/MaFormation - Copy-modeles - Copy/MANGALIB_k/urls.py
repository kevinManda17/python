from django.urls import path
from . import views

app_name="MANGALIB_k"

urlpatterns=[
    path('',views.index, name= 'index'),
    path('<int:book_id>/',views.show, name='show'),
    path('ajouter-livre/', views.add, name="Ajouter")
]