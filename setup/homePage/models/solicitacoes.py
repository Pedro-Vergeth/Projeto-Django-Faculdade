from django.db import models
from .managers import manager

class solicitacao(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    manager = models.ForeignKey(manager, on_delete=models.CASCADE)



