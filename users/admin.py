from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username', 'first_name', 'last_name', 'kurs', 'tuman', 'mfy', 't_yil', 'fakultet'
    ]
    search_fields = ['id', 'username', 'first_name', 'last_name', 'kurs', 'tuman','mfy', 'fakultet']
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

