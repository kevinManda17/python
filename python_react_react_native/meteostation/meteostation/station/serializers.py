from rest_framework import serializers
from .models import Station, Reading

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    readings = ReadingSerializer(many=True, read_only=True)

    class Meta:
        model = Station
        fields = '__all__'
