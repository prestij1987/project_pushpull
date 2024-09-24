from django.db import models
from datetime import datetime

# Create your models here.


class Event(models.Model):
    text = models.CharField(max_length = 1024)
    data = models.DateField(max_length= 100)
    itog = models.BooleanField(True)