# Generated by Django 4.1.6 on 2023-02-15 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_rename_user_ish_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ish',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='oliy_yurt',
            name='user',
        ),
    ]