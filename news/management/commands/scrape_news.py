from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from news.models import News

def scrape_news():
    url = 'https://www.fantasypros.com/nfl/breaking-news.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    boxes = soup.select('.ten.columns')

    for box in boxes[::2]: # every other box
        header = box.select_one('span')
        
        next_div = box.select_one('.ten.columns div') # div before description and impact

        description = next_div.find_next_sibling('p')
        fantasy_impact = description.find_next_sibling('p')        

        news_data = {
            'header': header.text,
            'description': description.text,
            'impact': fantasy_impact.text[16:],
        }
        
        news.append(news_data)

    return news

def save_news(news):
    for headline in news:
        header = news['header']
        description = news['description']
        fantasy_impact = news['impact']

        headline = News(header=header, description=description, fantasy_impact=fantasy_impact)
        headline.save()

class Command(BaseCommand):
    help = 'Scrape news data and save it to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        news = scrape_news()
        save_news()
        self.stdout.write("Finished scraping.")