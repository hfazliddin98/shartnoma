# Generated by Django 4.2.1 on 2023-06-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amaliyot', '0007_alter_amaliyot_talaba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amaliyot',
            name='b_sana',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='amaliyot',
            name='t_sana',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
