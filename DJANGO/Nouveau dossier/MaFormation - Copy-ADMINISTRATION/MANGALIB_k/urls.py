from django.urls import path
from . import views

app_name="MANGALIB_k"

urlpatterns=[
    path('',views.index, name= 'index'),
    path('<int:book_id>/',views.show, name='show'),
    path('add-books/', views.add, name ="add"),
    path("Edit-books/", views.edit, name="edit"),
    path("delete-books/",views.delete, name="Delete"),
]