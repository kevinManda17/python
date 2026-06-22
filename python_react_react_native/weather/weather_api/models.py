from django.db import models
from django.contrib.auth.models import User

class WeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']

        