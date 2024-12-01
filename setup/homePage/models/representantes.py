from django.db import models
from .managers import Manager

class Representante(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    neighborhood = models.CharField(max_length=255, null=False, blank=False)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)

    def check_password(self, raw_password): 
        return self.password == raw_password