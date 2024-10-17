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

'''def zapros(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/form_quest.html',  # put k shablonu
                                # podstanovka
        context
    )'''

from . import forms
def zapros(request):
    if request.method == "POST":
        form = forms.ZaprosForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': forms.ZaprosForm(),
    }
    return render(
        request,                  # Запрос
        'mainpage/form_quest.html',   # путь к шаблону
        context                   # подстановки
    )