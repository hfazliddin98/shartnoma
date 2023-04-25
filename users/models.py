from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sharif = models.CharField(max_length=100)
    t_yil = models.CharField(max_length=100)    
    t_nomer = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)         
    sana = models.DateTimeField(auto_now_add=True)
    
    
