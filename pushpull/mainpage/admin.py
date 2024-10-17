
from django.contrib import admin 
from . import models 
  
# Register your models here. 
 
@admin.register(models.Dist) 
class TaskAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Dist._meta.get_fields()]


@admin.register(models.Zapros) 
class ZaprosAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Zapros._meta.get_fields()]
