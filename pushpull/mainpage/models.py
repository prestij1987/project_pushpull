from django.db import models
from datetime import datetime

# Create your models here.

class Dist(models.Model):
    city_pogruz = models.CharField(max_length=1024)
    city_vygruz = models.CharField(max_length=1024)
    time_way = models.DateField(datetime.now())
    