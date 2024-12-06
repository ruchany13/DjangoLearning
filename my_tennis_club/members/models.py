from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
class Student(models.Model):
    adı = models.CharField(max_length=255)
    soyadı = models.CharField(max_length=255)
    yurt = models.CharField(max_length=255)
    sınıf = models.IntegerField(null=True)
    seviye = models.IntegerField(null=True)