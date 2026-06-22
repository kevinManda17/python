from django.urls import path 
from .views import morceau_detail , MorceauDetailView , MorceauList

app_name ="musiques"


urlpatterns = [
    
    path('<int:pk>/', MorceauDetailView.as_view() , name="morceau-detail"),
    path('', MorceauList.as_view(), name='morceau_list'),

]