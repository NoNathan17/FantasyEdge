from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from news.models import News
from django.db import IntegrityError

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

        previous_div = box.find_previous_sibling('div') # div that contains the player image

        try:
            image = previous_div.find('img')['src']
        except TypeError:
            image = 'https://static.vecteezy.com/system/resources/previews/020/911/740/non_2x/user-profile-icon-profile-avatar-user-icon-male-icon-face-icon-profile-icon-free-png.png'

        news_data = {
            'header': header.text,
            'description': description.text,
            'impact': fantasy_impact.text[16:],
            'image': image,
        }
        
        news.append(news_data)

    return news

def save_news(news):
    for item in reversed(news):
        try:
            header = item['header']
            description = item['description']
            fantasy_impact = item['impact']
            image = item['image']

            item = News(header=header, description=description, fantasy_impact=fantasy_impact, image=image)
            item.save()
        except IntegrityError:
            print(f'Header: "{header}" already exists. Not saving to database.')

class Command(BaseCommand):
    help = 'Scrape news data and save it to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        news = scrape_news()
        save_news(news)
        self.stdout.write("Finished scraping.")