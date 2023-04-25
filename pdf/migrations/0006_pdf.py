# Generated by Django 4.2 on 2023-04-25 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pdf', '0005_amaliyot_fakultet_viloyat_delete_ish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amaliyot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.amaliyot', unique=True)),
                ('fakultet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf.fakultet')),
                ('talaba_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
