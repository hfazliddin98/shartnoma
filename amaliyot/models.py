from django.db import models
from users.models import User

class Amaliyot(models.Model):
    viloyat_a = models.CharField(max_length=100)
    tuman_a = models.CharField(max_length=100)
    mfy_a = models.CharField(max_length=100)
    kocha_uy_a = models.CharField(max_length=100)
    muassasa = models.CharField(max_length=200)
    d_ism = models.CharField(max_length=100)
    d_nomeri = models.CharField(max_length=100)
    kurs = models.CharField(max_length=100)    
    a_rahbari =models.CharField(max_length=100)
    o_a_rahbari = models.CharField(max_length=100)
    a_turi = models.CharField(max_length=100)
    b_sana = models.CharField(max_length=100, blank=True)
    t_sana = models.CharField(max_length=100, blank=True)
    talaba = models.IntegerField()
    
    def __str__(self):
        return self.muassasa