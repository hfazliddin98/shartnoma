from django.db import models
from django.contrib.auth import get_user_model
from fakultet.models import Fakultetlar
from amaliyot.models import Amaliyot



class Pdf(models.Model):
    talaba_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fakultet_id = models.ForeignKey(Fakultetlar, on_delete=models.CASCADE)
    amaliyot_id = models.ForeignKey(Amaliyot, on_delete=models.CASCADE)

