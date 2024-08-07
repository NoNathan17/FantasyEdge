from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from rankings.models import Player, Quarterback, RunningBack, WideReciever, TightEnd, Kicker, Defense

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

        if cols[2].text[0] == 'D': # if position is defense
            end_split = 3

        team_index = 2
        bye_index = 3
        three_names = ['II', 'III', 'Jr.', 'Sr.', 'St.', 'Bay', 'Los', 'Kansas', 'New', 'Las', 'San']

        column_one = cols[1].text.split()
        try:
            if any(word in three_names for word in column_one[:3]): # if first name has 3 words
                team_index = 3
                bye_index = 4

            player_data = {
                'name': " ".join(cols[1].text.split()[0:team_index]),
                'team': cols[1].text.split()[team_index],
                'position': cols[2].text[0:end_split],
                'bye week': cols[1].text.split()[bye_index],
                'adp': cols[8].text,
                'info': f'https://www.fantasypros.com{cols[1].find("a")["href"]}'
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
        adp = player['adp']
        info = player['info']

        if not position == 'DST':
            player = Player(name=name, team=team, position=position, bye_week=bye_week, adp=adp, info=info)
            player.save()

        match position:
            case 'QB':
                quarterback = Quarterback(name=name, team=team, position=position, bye_week=bye_week, adp=adp, info=info)
                quarterback.save()
            case 'RB':
                runningback = RunningBack(name=name, team=team, position=position, bye_week=bye_week, adp=adp)
                runningback.save()
            case 'WR':
                widereciever = WideReciever(name=name, team=team, position=position, bye_week=bye_week, adp=adp, info=info)
                widereciever.save()
            case 'TE':
                tightend = TightEnd(name=name, team=team, position=position, bye_week=bye_week, adp=adp, info=info)
                tightend.save()
            case 'K':
                kicker = Kicker(name=name, team=team, position=position, bye_week=bye_week, adp=adp, info=info)
                kicker.save()
            case 'DST':
                defense = Defense(name=name, position=position, bye_week=bye_week, adp=adp, info=info)
                defense.save()

        
class Command(BaseCommand):
    help = 'Scrape player data and save it to database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        players = scrape_players()
        save_players(players)
        self.stdout.write("Finished scraping.")