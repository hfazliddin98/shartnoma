# Generated by Django 4.2.1 on 2023-05-20 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('amaliyot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amaliyot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amaliyot.amaliyot')),
            ],
        ),
    ]
