from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Player, Quarterback, RunningBack, WideReciever, TightEnd, Kicker, Defense

# Create your views here.
def rankings_view(request): 
    players = Player.objects.all()
    return render(request, 'overall_rankings.html', {'players': players})

def quarterback_view(request):
    quarterbacks = Quarterback.objects.all()
    return render(request, 'quarterback_rankings.html', {'quarterbacks': quarterbacks})

def runningback_view(request):
    runningbacks = RunningBack.objects.all()
    return render(request, 'runningback_rankings.html', {'runningbacks': runningbacks})

def widereciever_view(request):
    widerecievers = WideReciever.objects.all()
    return render(request, 'widereceiver_rankings.html', {'widerecievers': widerecievers})

def tightend_view(request):
    tightends = TightEnd.objects.all()
    return render(request, 'tightend_rankings.html', {'tightends': tightends})

def kicker_view(request):
    kickers = Kicker.objects.all()
    return render(request, 'kicker_rankings.html', {'kickers': kickers})

def defense_view(request):
    defenses = Defense.objects.all()
    return render(request, 'defense_rankings.html', {'defenses': defenses})

