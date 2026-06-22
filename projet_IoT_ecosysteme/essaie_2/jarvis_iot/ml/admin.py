# ml/admin.py
from django.contrib import admin
from .models import EnergyPrediction

@admin.register(EnergyPrediction)
class EnergyPredictionAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'predicted_consumption', 'actual_consumption')
    list_filter = ('timestamp',)
    search_fields = ('timestamp',)
