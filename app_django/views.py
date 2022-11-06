from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse('<h1>Index</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')


def yandex(request):
    return HttpResponseRedirect('http://yandex.ru')


def home(request):
    name = 'Мурат'
    howdoyoudo = 'Как поживаешь?'
    return render(request,'home.html',context={'name': name, 'how': howdoyoudo})