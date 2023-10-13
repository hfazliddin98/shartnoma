from django.contrib import admin
from .models import Pdf, Rasm

admin.site.register([Rasm])
class PdfAdmin(admin.ModelAdmin):
    list_display = [
        'id'
    ]
admin.site.register(Pdf, PdfAdmin)