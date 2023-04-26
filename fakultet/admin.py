from django.contrib import admin
from .models import Fakultet, Fakultetlar, Talim_turi, Yonalish, Kurs


admin.site.register([Fakultetlar,Fakultet,Talim_turi,Yonalish,Kurs])