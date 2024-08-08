from django.shortcuts import render
from .models import Team

# Create your views here.

def schedule_view(request):
    teams = Team.objects.all()
    return render(request, 'schedule.html', {'teams': teams})
