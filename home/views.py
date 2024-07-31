from django.shortcuts import HttpResponse
from django.template import loader
from .models import Player

# Create your views here.
def home(request):
    players = Player.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'players': players,
    }
    return HttpResponse(template.render(context, request))