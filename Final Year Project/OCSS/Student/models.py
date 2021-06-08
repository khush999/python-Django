from django.db import models
from django.db.models import Model
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    SID = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.PositiveIntegerField()
    birth_Date = models.DateField(auto_now=False, auto_now_add=False)
    # gender = models.IntegerField(choices=GENDER_CHOICES)
    mobile_no = models.PositiveIntegerField()
    enroll_No = models.PositiveIntegerField()
    clg_Name = models.CharField(max_length=50)
    # education
    # branch
    # passing_year
    cpi = models.PositiveIntegerField()
    cgpa = models.PositiveIntegerField()
    extra_skill = models.CharField(max_length=100)
    # resume
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50) 


class std_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  


