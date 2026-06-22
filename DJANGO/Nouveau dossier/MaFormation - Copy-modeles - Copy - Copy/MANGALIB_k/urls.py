from django.urls import path
from . import views

app_name="MANGALIB_k"

urlpatterns=[
    path('',views.index, name= 'index'),
    path('<int:book_id>/',views.show, name='show')
]