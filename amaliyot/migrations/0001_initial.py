# Generated by Django 4.2 on 2023-04-27 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viloyat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amaliyot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muassasa', models.CharField(max_length=200)),
                ('d_ism', models.CharField(max_length=100)),
                ('d_nomeri', models.CharField(max_length=100)),
                ('a_rahbari', models.CharField(max_length=100)),
                ('o_a_rahbari', models.CharField(max_length=100)),
                ('a_turi', models.CharField(max_length=100)),
                ('b_sana', models.CharField(max_length=100)),
                ('t_sana', models.CharField(max_length=100)),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viloyat.viloyatlar')),
            ],
        ),
    ]
