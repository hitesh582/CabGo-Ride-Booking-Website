from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse

# Create your models here.

class Cre_Acc(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(null=True, max_length=50)
    mobilenumber = models.IntegerField(null=True,validators=[MaxValueValidator(10)])
    email = models.CharField(null=True,max_length=50)
    password = models.CharField(null=True,max_length=50)
    username = models.CharField(null=True,max_length=50)



class publish_ride(models.Model):
    des1=models.CharField(null= True, max_length=50)
    des2=models.CharField(null=True, max_length=50)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    seats=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    carname=models.CharField(null=True, max_length=50)
    carnumber=models.CharField(null=True, max_length=10)
    license=models.CharField(null=True, max_length=50)