from django.db import models
from django.contrib.auth import get_user_model
from amaliyot.models import Amaliyot



class Pdf(models.Model):
    talaba_id = models.CharField(max_length=10, blank=True)
    shartnoma_raqami = models.CharField(max_length=100, blank=True)    
    talaba_f_i_sh = models.CharField(max_length=100, blank=True)
    talaba_manzil = models.CharField(max_length=100, blank=True)
    talaba_fakulteti = models.CharField(max_length=200, blank=True)
    talaba_yonalishi = models.CharField(max_length=100, blank=True)    
    talaba_kurs = models.CharField(max_length=100, blank=True)
    talaba_shifr = models.CharField(max_length=100, blank=True)
    talaba_nomer = models.CharField(max_length=200, blank=True)
    derektor_nomer = models.CharField(max_length=200, blank=True)   
    amaliyot_joyi = models.CharField(max_length=100, blank=True)    
    amaliyot_manzili = models.CharField(max_length=100, blank=True)
    amaliyot_rahbari = models.CharField(max_length=100, blank=True)    
    biriktirilgan_rahbar = models.CharField(max_length=100, blank=True)
    amaliyot_turi = models.CharField(max_length=100, blank=True)    
    amaliyot_boshlanishi = models.CharField(max_length=100, blank=True)
    amaliyot_tugashi = models.CharField(max_length=100, blank=True)    
    amaliyot_buyruq_raqami = models.CharField(max_length=100, blank=True)
    korxona_nomi = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.talaba_f_i_sh
    
    
class Rasm(models.Model):
    user_id = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='code/')
    
    def __str__(self):
        return self.link
    

