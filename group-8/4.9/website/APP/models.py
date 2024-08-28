from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
    name = models.CharField(verbose_name='ФИО клиента', max_length=30)
    number = PhoneNumberField(region="RU")
    email = models.EmailField(verbose_name='email', unique=True)
    def __str__(self):
        return self.name