from django.db import models
from django.forms import CharField

class Familiares(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    active = models.BooleanField(default=True)
    date = models.CharField(max_length=50, unique=True)
