from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'username'
    ]
    search_fields = ['id', 'username']
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

