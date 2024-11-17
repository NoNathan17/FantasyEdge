from django.shortcuts import render
from django.http import JsonResponse
from trade_analyzer.models import Player


# Create your views here.

def trade_analyzer_view(request):
    return render(request, 'trade_analyzer.html')

def compare_players(player_1: Player, player_2: Player) -> str:
    if player_1.rating > player_2.rating:
        return f"{player_1.name} wins the trade"
    elif player_1.rating < player_2.rating:
        return f"{player_2.name} wins the trade"
    else:
        return "The trade is a tie"
    
def compare_trade(request):
    if request.method == "POST":
        player_1_name = request.POST.get('player_1')
        player_2_name = request.POST.get('player_2')

        player_1 = Player.objects.get(name=player_1_name)
        player_2 = Player.objects.get(name=player_2_name)

        result = compare_players(player_1, player_2)

        return JsonResponse({'result': result})

        # return render(request, 'trade_analyzer.html', {'players': Player.objects.all(), 'result': result})

    else:
        # return render(request, 'trade_analyzer.html', {'players': Player.objects.all()})
        return JsonResponse({'error': "Invalid request."}, status=400)
