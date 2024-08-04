from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Quarterback, RunningBack, WideReciever, TightEnd, Kicker

# Create your views here.
def rankings_view(request): # need to find a way to reset the url when a new link is clicked
    quarterbacks = Quarterback.objects.all()
    runningbacks = RunningBack.objects.all()
    widerecievers = WideReciever.objects.all()
    tightends = TightEnd.objects.all()
    kickers = Kicker.objects.all()
    template = loader.get_template('rankings.html')
    context = {'quarterbacks': quarterbacks, 
               'runningbacks': runningbacks,
               'widerecievers': widerecievers,
               'tightends': tightends,
               'kickers': kickers,
               }
    return HttpResponse(template.render(context, request))    

def quarterback_view(request):
    quarterbacks = Quarterback.objects.all()
    return render(request, 'quarterback_rankings.html', {'quarterbacks': quarterbacks})

def runningback_view(request):
    runningbacks = RunningBack.objects.all()
    return render(request, 'runningback_rankings.html', {'runningbacks': runningbacks})

def widereciever_view(request):
    widereceivers = WideReciever.objects.all()
    return render(request, 'widereceiver_rankings.html', {'widereceivers': widereceivers})

def tightend_view(request):
    tightends = TightEnd.objects.all()
    return render(request, 'tightend_rankings.html', {'tightends': tightends})

def kicker_view(request):
    kickers = Kicker.objects.all()
    return render(request, 'kicker_rankings.html', {'kickers': kickers})

