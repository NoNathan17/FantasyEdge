from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

def scrape_players():
    url = 'https://www.fantasypros.com/nfl/adp/ppr-overall.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    players = []
    table = soup.select_one('table')
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        
        end_split = 2
        if cols[2].text[0] == 'K':
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

    print(players)


scrape_players()