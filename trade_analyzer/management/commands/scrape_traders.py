from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from trade_analyzer.models import Player
from django.db import IntegrityError

def scrape_players() -> list[dict]:
    url = 'https://www.footballguys.com/rankings/duration/restofseason'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    players = []
    table = soup.select_one('table')
    for row in table.find_all('tr')[2:]:
        spans = row.find_all('span')
        cols = row.find_all('td')
        if row.select_one('b') != None:
            name = row.select_one('b').text
        if len(spans) == 2:
            team = spans[0].text
            position = spans[1].text[:2]
        if len(cols) == 10:
            rating = cols[4].text

        print(name, team, position, rating)

        player_data = {
            'name': name,
            'team': team,
            'position': position,
            'rating': rating
        }    
        players.append(player_data)

    return players    

def save_players(players: dict):
    for player in players:
        name = player['name']
        team = player['team']
        position = player['position']
        rating = player['rating']

        try:
            player = Player(name=name, team=team, position=position, rating=rating)
            player.save()
        except IntegrityError:
            print(f'Player: {name} already exists. Not saving to database')

class Command(BaseCommand):
    help = 'Scrape player data and save it to database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        players = scrape_players()
        save_players(players)
        self.stdout.write("Finished scraping.")