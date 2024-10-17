

from django.urls import path
from . import views 


#from .views import func_start

urlpatterns = [
    path('', views.index, name='home'),
    #path('mystring/', func_start, name='mystring'),
  
    path('uslugi/', views.uslugi, name='uslugi'),
    path('forma/', views.zapros, name='zapros'),


]
