from django.db import models
from .managers import manager

class representante(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.TextField(255)
    neighborhood = models.CharField()
    manager = models.ForeignKey(manager, on_delete=models.CASCADE)