from django.contrib import admin
from .models import Sensor, SensorData

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sensor_type', 'location', 'created_at')
    search_fields = ('name', 'sensor_type', 'location')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'value', 'timestamp')
    list_filter = ('sensor', 'timestamp')
    search_fields = ('sensor__name',)
