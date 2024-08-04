from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from rankings.models import Quarterback, RunningBack, WideReciever, TightEnd, Kicker

def scrape_players() -> list[dict]:
    url = 'https://www.fantasypros.com/nfl/adp/ppr-overall.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    players = []
    table = soup.select_one('table')
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        
        end_split = 2 
        if cols[2].text[0] == 'K': # if position is kicker
            end_split = 1

        try:
            player_data = {
                'name': cols[1].text.split()[0] + ' ' + cols[1].text.split()[1],
                'team': cols[1].text.split()[2],
                'position': cols[2].text[0:end_split],
                'bye week': cols[1].text.split()[3]
            }
            players.append(player_data)
        except IndexError:
            continue

    return players

def save_players(players): #saves players to the database by position
    for player in players:
        name = player['name']
        team = player['team']
        position = player['position']
        bye_week = player['bye week']

        match position:
            case 'QB':
                quarterback = Quarterback(name=name, team=team, position=position, bye_week=bye_week)
                quarterback.save()
            case 'RB':
                runningback = RunningBack(name=name, team=team, position=position, bye_week=bye_week)
                runningback.save()
            case 'WR':
                widereciever = WideReciever(name=name, team=team, position=position, bye_week=bye_week)
                widereciever.save()
            case 'TE':
                tightend = TightEnd(name=name, team=team, position=position, bye_week=bye_week)
                tightend.save()
            case 'K':
                kicker = Kicker(name=name, team=team, position=position, bye_week=bye_week)
                kicker.save()

        

class Command(BaseCommand):
    help = 'Scrape player data and save it to database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        players = scrape_players()
        save_players(players)
        self.stdout.write("Finished scraping.")