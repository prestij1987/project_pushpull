from django.shortcuts import render
from django.http import HttpResponse
#from .templates.tasklist import index

# Create your views here.

def func_start(request):
    return render(request, 'index.html')
print('index.html')


def index(request):
    context = {}
    return render(
        request,   # zapros
        'tasklist/index.html/',  # put k shablonu
                                # podstanovka
        context
    )