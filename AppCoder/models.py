from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=20)
    commission = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail = models.EmailField()


class Professor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail = models.EmailField()
    profession = models.CharField(max_length=30)


class Homework(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    handed_in = models.BooleanField()
