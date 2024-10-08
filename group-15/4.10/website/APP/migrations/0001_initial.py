# Generated by Django 5.1 on 2024-08-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО студента')),
                ('number', models.CharField(max_length=15, unique=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('date', models.DateField(verbose_name='Дата начала обучения')),
                ('pyth', models.BooleanField(default=True, verbose_name='Python')),
                ('math', models.BooleanField(verbose_name='Математика')),
                ('js', models.BooleanField(verbose_name='JavaScript')),
            ],
        ),
    ]
