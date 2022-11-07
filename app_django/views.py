from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddressForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        street = request.POST.get("street")
        return HttpResponse('{0} {1}'.format(name, street))

    else:
        addressform = AddressForm()
        return render(request, 'index.html', {'form': addressform})
    # return HttpResponse('<h1>Index</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')


def yandex(request):
    return HttpResponseRedirect('http://yandex.ru')


def home(request):
    name = 'Мурат!'
    howdoyoudo = 'Как поживаешь?'
    return render(request, 'home.html', context={'name': name, 'how': howdoyoudo})

