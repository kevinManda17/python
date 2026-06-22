from django.db import models

class EnergyPrediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    predicted_consumption = models.FloatField()
    actual_consumption = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} - Pred: {self.predicted_consumption}"
