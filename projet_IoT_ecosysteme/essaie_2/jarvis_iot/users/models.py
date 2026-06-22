from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('parent', 'Parent'),
        ('resident', 'Resident'),
        ('technician', 'Technician'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return self.username
