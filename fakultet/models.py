from django.db import models


class Yonalish(models.Model):
    yonalish = models.CharField(max_length=100)

class Kurs(models.Model):
    kurs = models.CharField(max_length=100)

class Talim_turi(models.Model):
    t_turi = models.CharField(max_length=100)

class Fakultet(models.Model):
    fakultet = models.CharField(max_length=100)
    
class Fakultetlar(models.Model):
    fakultet_id = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    yonalish_id = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    guruh = models.CharField(max_length=100)
