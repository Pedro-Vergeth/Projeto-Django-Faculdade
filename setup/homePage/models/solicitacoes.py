from django.db import models
from .managers import Manager

class Solicitacao(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    date = models.DateField(null=False)
    status = models.TextField(max_length=255, default='Pendente')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)



