from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str___(self):
        return self.name
    
class Menufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    def __str___(self):
        return self.name
    