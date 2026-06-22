from rest_framework import serializers
from .models import Sensor, SensorData

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class SensorDataSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensor', write_only=True)

    class Meta:
        model = SensorData
        fields = ["id", "sensor", "sensor_id", "value", "timestamp"]
