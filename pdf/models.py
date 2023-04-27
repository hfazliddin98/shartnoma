from django.db import models
from django.contrib.auth import get_user_model
from amaliyot.models import Amaliyot



class Pdf(models.Model):
    talaba_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    amaliyot_id = models.ForeignKey(Amaliyot, on_delete=models.CASCADE)

