# Generated by Django 4.2.2 on 2023-09-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amaliyot', '0009_alter_amaliyot_mfy_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amaliyot',
            name='muassasa',
            field=models.CharField(max_length=400),
        ),
    ]
