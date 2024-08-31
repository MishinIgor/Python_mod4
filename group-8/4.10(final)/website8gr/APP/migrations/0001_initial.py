# Generated by Django 5.1 on 2024-08-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО клиента')),
                ('number', models.CharField(max_length=15, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('inform', models.BooleanField(verbose_name='Информатика')),
                ('math', models.BooleanField(verbose_name='Математика')),
                ('phiz', models.BooleanField(verbose_name='Физика')),
            ],
        ),
    ]