from django.contrib import admin
from .models import Pdf, Rasm

admin.site.register([Rasm])
class PdfAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'talaba_id'
    ]
    search_fields = ['talaba_id']
admin.site.register(Pdf, PdfAdmin)