from django.db import models


class Oliy_yurt(models.Model):
    familya = models.CharField(max_length=200)
    ism = models.CharField(max_length=200)
    shahar = models.CharField(max_length=200)
    sana = models.DateTimeField(auto_now_add=True)



class Ish(models.Model):
    familya = models.CharField(max_length=200)
    ism = models.CharField(max_length=200)
    shahar = models.CharField(max_length=200)
    sana = models.DateTimeField(auto_now_add=True)
