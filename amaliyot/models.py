from django.db import models
from viloyat.models import Viloyatlar

class Amaliyot(models.Model):
    viloyat = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    muassasa = models.CharField(max_length=200)
    d_ism = models.CharField(max_length=100)
    d_nomeri = models.CharField(max_length=100)
    a_rahbari =models.CharField(max_length=100)
    o_a_rahbari = models.CharField(max_length=100)
    a_turi = models.CharField(max_length=100)
    b_sana = models.CharField(max_length=100)
    t_sana = models.CharField(max_length=100)