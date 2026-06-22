from django.urls import path 
from . import views

app_name ='manga'

urlpatterns =[
    path('', views.index , name ="index"),
    path('<int:book_id>/' ,views.show , name='show'),
    path('add-books/',views.add , name='add'),
    path("edit-books/<int:book_id>/", views.edit , name="edit"),
    path("delete-books/<int:book_id>/", views.remove , name="remove"),
    
]