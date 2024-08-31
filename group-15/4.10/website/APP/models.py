from django.db import models

class Student(models.Model):
    name = models.CharField(verbose_name='ФИО студента', max_length=100)
    number = models.CharField(verbose_name='Телефон', max_length=15,unique=True)
    email = models.EmailField(verbose_name='email',unique=True)
    pyth = models.BooleanField(verbose_name='Python',default=True)
    math = models.BooleanField(verbose_name='Математика')
    js = models.BooleanField(verbose_name='JavaScript')
    def __str__(self):
        return self.name
    
    
