from django.shortcuts import render
import requests

# Create your views here.
def fetch_data(request):
    url = 'https://api.fantasynerds.com/v1/nfl/tiers?apikey=TEST&format='
    response = requests.get(url)
    players = response.json()
