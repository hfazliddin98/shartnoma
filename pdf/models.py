from django.db import models
from django.contrib.auth import get_user_model



class Fakultet(models.Model):
    fakultet = models.CharField(max_length=100)
    kafedra = models.CharField(max_length=100)
    guruh = models.CharField(max_length=100)
    kurs = models.CharField(max_length=100)
    talim_turi = models.CharField(max_length=100)


class Viloyat(models.Model):
    viloyat = models.CharField(max_length=100)
    tuman = models.CharField(max_length=100)
    mfy = models.CharField(max_length=100)
    kocha_uy = models.CharField(max_length=200)

class Amaliyot(models.Model):
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    muassasa = models.CharField(max_length=200)
    d_ism = models.CharField(max_length=100)
    d_nomeri = models.CharField(max_length=100)
    a_rahbari =models.CharField(max_length=100)
    o_a_rahbari = models.CharField(max_length=100)
    a_turi = models.CharField(max_length=100)
    b_sana = models.CharField(max_length=100)
    t_sana = models.CharField(max_length=100)

class Pdf(models.Model):
    talaba_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fakultet_id = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    amaliyot_id = models.ForeignKey(Amaliyot, on_delete=models.CASCADE)

