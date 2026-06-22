from django.urls import path
from .views import (
    StationListCreateView,
    StationDetailView,
    PredictView,
)

urlpatterns = [
    # CRUD Stations
    path('stations/', StationListCreateView.as_view(), name='stations-list-create'),
    path('stations/<int:pk>/', StationDetailView.as_view(), name='stations-detail'),

    # Prédiction météo via ML
    path('predict/', PredictView.as_view(), name='predict'),
]
