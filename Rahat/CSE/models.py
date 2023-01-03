from django.db import models
from django import forms


# Create your models here.
#create a model for the database
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=200)
    batch = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    address = models.TextField()
    blood_group = models.CharField(max_length=100)
    last_donated = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/', blank=True)
    cgpa= models.FloatField()
    

    def __str__(self):
        return self.name

class User(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email= models.EmailField()
    blood_group= models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    joining_date=models.DateField()
    sales_count=models.IntegerField()
    city= models.CharField(max_length=255)
    division= models.CharField(max_length=255)
    address= models.TextField()
    post_code= models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name+'( '+ self.phone +')'

