from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from schedule.models import Team

def scrape_schedules() ->list[dict]:
    url = 'https://www.fantasypros.com/nfl/schedule.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    teams = []
    tables = soup.find_all('table')
    for table in tables:
        name = " ".join(table.find('caption').text.split()[1:-1])

        table_body = table.find('tbody')
        cols = table_body.find_all('td')
        opponents = []
        for col in cols:
            opponent = col.text.replace('\n', '')
            opponents.append(opponent)
        
        team_data = {
            'name': name,
            'opponents': opponents,
        }

        teams.append(team_data)

    return teams

def save_schedules(teams):
    for team in teams:
        name = team['name']
        opponents = team['opponents']

        team = Team(name=name, opponents=opponents)
        team.save()

class Command(BaseCommand):
    help = 'Scrape schedule data and save it to database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        teams = scrape_schedules()
        save_schedules(teams)
        self.stdout.write("Finished scraping.")

