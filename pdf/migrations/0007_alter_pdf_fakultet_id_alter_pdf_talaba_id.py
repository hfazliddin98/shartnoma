# Generated by Django 4.2 on 2023-04-25 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pdf', '0006_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='fakultet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.fakultet', unique=True),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='talaba_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]