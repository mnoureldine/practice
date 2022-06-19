from django.db import models

# Create your models here.
from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    #ID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} [{self.email}]"