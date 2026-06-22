from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpertRuleViewSet

router = DefaultRouter()
router.register(r'rules', ExpertRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
