from django.db import models

# Create your models here.

class Faculty(models.Model):
    FID = models.AutoField(primary_key=True)
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=50)
    clg_name = models.CharField(max_length=100,default=str)
    Password = models.CharField(max_length=30)
  

class faculty_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)     

class review_std(models.Model):
    s_name = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

