from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Sensor, SensorData
from .serializers import SensorSerializer, SensorDataSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all().order_by('-timestamp')
    serializer_class = SensorDataSerializer
