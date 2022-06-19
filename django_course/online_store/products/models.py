import os
from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.name}"
