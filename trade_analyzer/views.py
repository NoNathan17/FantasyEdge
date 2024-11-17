from django.shortcuts import render
from trade_analyzer.models import Player

# Create your views here.

def trade_analyzer_view(request):
    return render(request, 'trade_analyzer.html')

def compare_players(player_1, player_2):
    if player_1.rating > player_2.rating:
        return f"{player_1.name} wins the trade"
    elif player_1.rating < player_2.rating:
        return f"{player_2.name} wins the trade"
    else:
        return "The trade is a tie"
    
def compare_trade(request):
    if request.method == "POST":
        # Get selected player IDs from the form
        player_1_id = request.POST.get('player_1')
        player_2_id = request.POST.get('player_2')

        # Retrieve the players from the database
        try:
            player_1 = Player.objects.get(id=player_1_id)
            player_2 = Player.objects.get(id=player_2_id)

            # Call the compare_players function
            result = compare_players(player_1, player_2)

        except Player.DoesNotExist:
            result = "One or both players do not exist."

        # Return the result along with players list to the template
        return render(request, 'trade_analyzer.html', {'players': Player.objects.all(), 'result': result})

    else:
        return render(request, 'trade_analyzer.html', {'players': Player.objects.all()})
    
