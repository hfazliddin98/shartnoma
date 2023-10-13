from django.contrib import admin
from .models import Amaliyot



class AmaliyotAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'talaba', 'viloyat_a', 'muassasa', 'tuman_a'
    ]
    search_fields = ['talaba', 'tuman_a',  'muassasa']

admin.site.register(Amaliyot, AmaliyotAdmin)