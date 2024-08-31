from django.db import models

class Client(models.Model):
    name = models.CharField(verbose_name='ФИО клиента', max_length=100)
    number = models.CharField(verbose_name='Номер телефона', max_length=15,unique=True)
    email = models.EmailField(verbose_name='email',unique=True)
    inform = models.BooleanField(verbose_name="Информатика")
    math = models.BooleanField(verbose_name="Математика")
    phiz = models.BooleanField(verbose_name="Физика")
    def __str__(self):
        return self.name