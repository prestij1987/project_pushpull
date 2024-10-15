from django.contrib import admin

# Register your models here.


from django.contrib import admin 
from .models import Dist
  
# Register your models here. 
 
@admin.register(Dist) 
class TaskAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Dist._meta.get_fields()]