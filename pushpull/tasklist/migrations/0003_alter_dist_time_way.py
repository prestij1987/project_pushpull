# Generated by Django 5.0.6 on 2024-10-01 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0002_dist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dist',
            name='time_way',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 14, 37, 35, 31839)),
        ),
    ]
