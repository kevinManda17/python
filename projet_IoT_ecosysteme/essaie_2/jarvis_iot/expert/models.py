from django.db import models

class ExpertDecision(models.Model):
    rule_name = models.CharField(max_length=100)
    condition = models.TextField()
    action = models.TextField()

    def __str__(self):
        return self.rule_name

# Si tu veux vraiment une classe Rule, il faut la créer :
class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
