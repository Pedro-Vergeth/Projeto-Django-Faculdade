from django.db import models

class manager(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.TextField(max_length=255)
    