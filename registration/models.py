from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=20,default="")
    last_name = models.CharField(max_length=20,default="")
    email = models.EmailField(max_length=18)
    password = models.CharField(max_length=128) 

class Meta:
    verbose_name_plural="Regisration"
7:52
