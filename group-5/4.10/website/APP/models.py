from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Student(models.Model):
    name = models.CharField(verbose_name='ФИО студента', max_length=100)
    number = PhoneNumberField(region='RU')
    email = models.EmailField(verbose_name='email',unique=True)
    pyth = models.BooleanField(verbose_name='Python',default=True)
    js = models.BooleanField(verbose_name='JavaScript')
    math = models.BooleanField(verbose_name='Математика')
    def __str__(self):
        return self.name
