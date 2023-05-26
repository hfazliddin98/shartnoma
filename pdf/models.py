from django.db import models
from django.contrib.auth import get_user_model
from amaliyot.models import Amaliyot



class Pdf(models.Model):
    talaba_id = models.CharField(max_length=100)    
    amaliyot_id = models.CharField(max_length=100)

