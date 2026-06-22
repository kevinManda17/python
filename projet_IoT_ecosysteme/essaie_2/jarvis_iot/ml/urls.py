from django.urls import path
from .views import EnergyPredictView

urlpatterns = [
    path('predict/', EnergyPredictView.as_view(), name='predict_energy'),
]
