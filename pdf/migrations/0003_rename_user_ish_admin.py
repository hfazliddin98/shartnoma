# Generated by Django 4.1.6 on 2023-02-14 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_rename_ish_beruvchi_ish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ish',
            old_name='user',
            new_name='admin',
        ),
    ]
