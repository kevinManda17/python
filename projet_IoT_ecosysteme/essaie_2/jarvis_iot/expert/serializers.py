from rest_framework import serializers
from .models import ExpertDecision

class ExpertRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertDecision
        fields = "__all__"
