from django.contrib import admin
from .models import Rule, ExpertDecision

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')  # champs existants
    list_filter = ('created_at',)

@admin.register(ExpertDecision)
class ExpertDecisionAdmin(admin.ModelAdmin):
    list_display = ('rule_name', 'condition', 'action')  # champs existants
    list_filter = ('rule_name',)
