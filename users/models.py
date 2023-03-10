from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    sharif = models.CharField('Sharif', max_length=100)
    t_yil = models.CharField('Sharif', max_length=100)
    yonalish = models.CharField('Talim yo`nalishii', max_length=200)
    k_yil = models.CharField('Kirgan yili', max_length=200)
    viloyat = models.CharField('Viloyat', max_length=200)
    shahar = models.CharField('Shahar tuman', max_length=200)
    kocha = models.CharField('Ko`cha nomi', max_length=200)
    uy_nomer = models.CharField('Uy nomer', max_length=200)
    telefon = models.CharField('Telefon raqam', max_length=200)
    familya_i = models.CharField('Familya', max_length=200) 
    ism_i = models.CharField('Familya', max_length=200)    
    sharif_i = models.CharField('Familya', max_length=200)       
    sana = models.DateTimeField(auto_now_add=True)
    
    
