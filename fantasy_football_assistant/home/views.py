from django.shortcuts import HttpResponse, render
from django.template import loader
# from .models import Player

# Create your views here.
def home(request):
    return render(request, 'home.html')