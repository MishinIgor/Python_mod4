from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos')
    telegram = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    profession = models.CharField(max_length=50)
    bio = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.profession}"
