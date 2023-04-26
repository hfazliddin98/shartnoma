from django.db import models



class Viloyat(models.Model):
    viloyat = models.CharField(max_length=100)   
    

class Tuman(models.Model):
    tuman = models.CharField(max_length=100)


class Viloyatlar(models.Model):
    viloyat_id = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tumam_id = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    mfy = models.CharField(max_length=100)
    kocha_uy = models.CharField(max_length=200)