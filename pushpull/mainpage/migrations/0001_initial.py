# Generated by Django 5.0.6 on 2024-10-17 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_pogruz', models.CharField(max_length=1024)),
                ('city_vygruz', models.CharField(max_length=1024)),
                ('time_way', models.DateField(verbose_name=datetime.datetime(2024, 10, 17, 17, 51, 41, 543376))),
            ],
        ),
        migrations.CreateModel(
            name='Zapros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
