from django.shortcuts import render
#from django.http import HttpResponse



def index(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/index.html',  # put k shablonu
                                # podstanovka
        context
    )

def uslugi(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/uslugi.html',  # put k shablonu
                                # podstanovka
        context
    )