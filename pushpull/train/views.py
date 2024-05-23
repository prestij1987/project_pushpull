from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def func_start(response):
    return HttpRequest('My two string')
print('index.html')
