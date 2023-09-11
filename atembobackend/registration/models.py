from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128) 

      
    def __str__(self):
         return  self.first_name
    


 
