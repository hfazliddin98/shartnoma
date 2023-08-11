from django.contrib import admin
from .models import Amaliyot



class AmaliyotAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'talaba', 'viloyat_a', 'muassasa'
    ]
    search_fields = ['talaba']

admin.site.register(Amaliyot, AmaliyotAdmin)