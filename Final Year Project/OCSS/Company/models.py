
from django.db import models

# Create your models here.
class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    email = models.EmailField(max_length=40)
    cp_name = models.CharField(max_length=20)
    c_website = models.URLField(blank=True)
    contact_no = models.CharField(max_length=15)

    class Meta:
        db_table = "company"
    
    # def __str__(self):
    #     return self.c_name


class comp_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)    


class Companyac(models.Model):
    c_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    date = models.DateField()
    contact_no = models.CharField(max_length=15)

    class Meta:
        db_table = "companyac"
    
    # def __str__(self):
    #     return self.c_name

class addnewjob(models.Model):
    c_name = models.CharField(max_length=50)
    # catagory = models.Choices()
    # role
    # min_qualification
    # req_skill=
    extra_skill = models.CharField(max_length=100)
    # max_age
    # job_location
    # salary
    working_hour = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    la_date = models.DateField(auto_now=False, auto_now_add=False)


     
       
