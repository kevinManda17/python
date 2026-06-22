from django.db import models

class AgentCommand(models.Model):
    command = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command


class AgentResponse(models.Model):
    command = models.ForeignKey(AgentCommand, on_delete=models.CASCADE, related_name='responses')
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.command.command}"
