from django.db import models
from django.contrib.auth.models import AbstractUser
from fakultet.models import Talim_turi, Fakultet, Yonalish
from viloyat.models import Viloyat, Tuman

class User(AbstractUser):
    sharif = models.CharField(max_length=100)
    t_yil = models.CharField(max_length=100)    
    t_nomer = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    talim_turi = models.CharField(max_length=100)
    fakultet = models.CharField(max_length=100)
    yonalish = models.CharField(max_length=100)
    guruh = models.CharField(max_length=100)
    viloyat = models.CharField(max_length=100)
    tuman = models.CharField(max_length=100)
    mfy = models.CharField(max_length=100)   
    kocha_uy = models.CharField(max_length=100)    
    
    
    
