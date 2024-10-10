from django.shortcuts import render, HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Player, Quarterback, RunningBack, WideReciever, TightEnd, Kicker, Defense

# Create your views here.
def rankings_view(request): 
    players = Player.objects.all()
    paginator = Paginator(players, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'overall_rankings.html', {'page_obj': page_obj})

def quarterback_view(request):
    quarterbacks = Quarterback.objects.all()
    paginator = Paginator(quarterbacks, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'quarterback_rankings.html', {'page_obj': page_obj})

def runningback_view(request):
    runningbacks = RunningBack.objects.all()
    paginator = Paginator(runningbacks, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    
    return render(request, 'runningback_rankings.html', {'page_obj': page_obj})

def widereciever_view(request):
    widerecievers = WideReciever.objects.all()
    paginator = Paginator(widerecievers, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'widereceiver_rankings.html', {'page_obj': page_obj})

def tightend_view(request):
    tightends = TightEnd.objects.all()
    paginator = Paginator(tightends, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'tightend_rankings.html', {'page_obj': page_obj})

def kicker_view(request):
    kickers = Kicker.objects.all()
    paginator = Paginator(kickers, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'kicker_rankings.html', {'page_obj': page_obj})

def defense_view(request):
    defenses = Defense.objects.all()
    paginator = Paginator(defenses, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'defense_rankings.html', {'page_obj': page_obj})

