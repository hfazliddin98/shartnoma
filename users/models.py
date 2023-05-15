from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sharif = models.CharField(max_length=100)
    t_yil = models.CharField(max_length=100, blank=True)    
    t_nomer = models.CharField(max_length=200)
    k_yil = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    talim_turi = models.CharField(max_length=100, blank=True)
    fakultet = models.CharField(max_length=100, blank=True)
    yonalish = models.CharField(max_length=100, blank=True)
    kurs = models.CharField(max_length=10, blank=True)
    guruh = models.CharField(max_length=100, blank=True)
    viloyat = models.CharField(max_length=100)
    tuman = models.CharField(max_length=100)
    mfy = models.CharField(max_length=100, blank=True)   
    kocha_uy = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100, blank=True)
    # dekanat
    dekanat_fakultet = models.CharField(max_length=100, blank=True)
    dekanat_kafedra = models.CharField(max_length=100, blank=True)

    parol = models.CharField(max_length=100)    
    
    
    
