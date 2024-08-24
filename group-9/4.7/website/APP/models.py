from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    data_expl = models.DateTimeField()

class Category(models.Model):
    title = models.CharField(max_length=100)
    lots = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    status = models.BooleanField()
    category = models.CharField(max_length=100)
    type_category = models.CharField(max_length=100)
    study = models.CharField(max_length=100)

class Student(models.Model):
    course_age = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    educ_prog_numb = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    lots = models.IntegerField()
    teacher = models.CharField(max_length=100)
    
class Group(models.Model):
    lots = models.IntegerField()
    Tutor = models.CharField(max_length=100)
    number = models.IntegerField()
    
    
