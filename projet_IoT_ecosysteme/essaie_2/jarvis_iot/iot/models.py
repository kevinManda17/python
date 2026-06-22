from django.db import models

class Sensor(models.Model):
    SENSOR_TYPES = (
        ('temperature', 'Temperature'),
        ('voltage', 'Voltage'),
        ('light', 'Light'),
        ('motion', 'Motion'),
    )
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=50, choices=SENSOR_TYPES)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.sensor_type})"

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="data")
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.name}: {self.value} at {self.timestamp}"
