from django.contrib import admin
from .models import AgentCommand, AgentResponse

@admin.register(AgentCommand)
class AgentCommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'command', 'description', 'created_at')
    search_fields = ('command', 'description')

@admin.register(AgentResponse)
class AgentResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'command', 'response_text', 'created_at')
    list_filter = ('command',)
