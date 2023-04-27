from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'telefon', 'sana','password')

admin.site.unregister(Group)
admin.site.register(User)