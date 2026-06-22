from rest_framework import viewsets
from .models import ExpertDecision
from .serializers import ExpertRuleSerializer

class ExpertRuleViewSet(viewsets.ModelViewSet):
    queryset = ExpertDecision.objects.all()
    serializer_class = ExpertRuleSerializer
