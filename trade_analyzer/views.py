from django.shortcuts import render
from django.http import JsonResponse
from trade_analyzer.models import Player


# Create your views here.

def trade_analyzer_view(request):
    return render(request, 'trade_analyzer.html')

def compare_players(players_giving: list, players_getting: list) -> str:
    giving_rating = sum(player.rating for player in players_giving)
    getting_rating = sum(player.rating for player in players_getting)
    if giving_rating > getting_rating:
        return f"Team 1 wins the trade"
    elif giving_rating < getting_rating:
        return f"Team 2 wins the trade"
    else:
        return "The trade is a tie"
    
def compare_trade(request):
    if request.method == "POST":
        giving_names = request.POST.getlist('giving[]')
        getting_names = request.POST.getlist('getting[]')

        players_giving = Player.objects.filter(name__in=giving_names)
        players_getting = Player.objects.filter(name__in=getting_names)

        result = compare_players(players_giving, players_getting)

        return JsonResponse({'result': result})


    else:
        return JsonResponse({'error': "Invalid request."}, status=400)
