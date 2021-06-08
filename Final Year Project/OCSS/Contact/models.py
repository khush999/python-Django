from django.db import models

# Create your models here.
class contact(models.Model):
    FID = models.AutoField(primary_key=True)
    F_name = models.CharField(max_length=50)
    L_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    msg = models.CharField(max_length=250)