from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Student(models.Model):
    CHOICES = [('1', 'М'), ('2','Ж')]
    name = models.CharField(verbose_name='ФИО студента', max_length=100)
    number = PhoneNumberField(region='RU')
    email = models.EmailField(verbose_name='email', unique=True)
    pyth = models.BooleanField(verbose_name='Python',default=True)
    js = models.BooleanField(verbose_name='JS')
    cpp = models.BooleanField(verbose_name='C++')
    gender = models.CharField(choices=CHOICES, max_length=128)
    def __str__(self):
        return self.name