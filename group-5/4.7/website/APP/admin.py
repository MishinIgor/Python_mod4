from django.contrib import admin
from .models import *

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Menufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    