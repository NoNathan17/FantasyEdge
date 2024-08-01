from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Quarterback, RunningBack, WideReciever, TightEnd, Kicker

# Create your views here.
def rankings_view(request):
    quarterbacks = Quarterback.objects.all()
    template = loader.get_template('rankings.html')
    context = {'quarterbacks': quarterbacks,}
    return HttpResponse(template.render(context, request))
