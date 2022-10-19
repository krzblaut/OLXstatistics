from django.shortcuts import render
from django.http import HttpResponse
from .models import Stats


# Create your views here.
def index(request):
    data = Stats.objects.all().filter(city_id=0)
    current = Stats.objects.all().filter(city_id=0).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/index.html', context)

def krakow(request):
    data = Stats.objects.all().filter(city_id=8959)
    current = Stats.objects.all().filter(city_id=8959).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/krakow.html', context)

def katowice(request):
    data = Stats.objects.all().filter(city_id=7691)
    current = Stats.objects.all().filter(city_id=7691).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/katowice.html', context)

def warszawa(request):
    data = Stats.objects.all().filter(city_id=17871)
    current = Stats.objects.all().filter(city_id=17871).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/warszawa.html', context)

def wroclaw(request):
    data = Stats.objects.all().filter(city_id=19701)
    current = Stats.objects.all().filter(city_id=19701).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/wroclaw.html', context)

def rzeszow(request):
    data = Stats.objects.all().filter(city_id=15241)
    current = Stats.objects.all().filter(city_id=15241).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/rzeszow.html', context)

def lodz(request):
    data = Stats.objects.all().filter(city_id=10609)
    current = Stats.objects.all().filter(city_id=10609).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/lodz.html', context)

def kielce(request):
    data = Stats.objects.all().filter(city_id=7971)
    current = Stats.objects.all().filter(city_id=7971).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/kielce.html', context)

def gdansk(request):
    data = Stats.objects.all().filter(city_id=5659)
    current = Stats.objects.all().filter(city_id=5659).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/gdansk.html', context)

def szczecin(request):
    data = Stats.objects.all().filter(city_id=16705)
    current = Stats.objects.all().filter(city_id=16705).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/szczecin.html', context)

def lublin(request):
    data = Stats.objects.all().filter(city_id=10119)
    current = Stats.objects.all().filter(city_id=10119).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/lublin.html', context)

def bydgoszcz(request):
    data = Stats.objects.all().filter(city_id=4019)
    current = Stats.objects.all().filter(city_id=4019).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/bydgoszcz.html', context)

def bialystok(request):
    data = Stats.objects.all().filter(city_id=1079)
    current = Stats.objects.all().filter(city_id=1079).latest('date') 
    context = {
        'data': data,
        'current': current,
    }
    return render(request, 'dashboard/bialystok.html', context)