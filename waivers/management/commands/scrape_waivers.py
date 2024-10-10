from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from waivers.models import Waiver

def scrape_waivers() -> list[dict]:
    options = Options()
    options.headless = True
    service = Service('/Users/nathanong/Desktop/fantasy-football-assistant/chromedriver-mac-x64/chromedriver')

    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.fantasypros.com/nfl/rankings/waiver-wire-ppr-overall.php'
    driver.get(url)

    waivers = []
    
    try:
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table'))
        )
        print(table.get_attribute('outerHTML'))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()



class Command(BaseCommand):
    help = 'Scrape waiver data and save it to database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting scraping...")
        waivers = scrape_waivers()
        self.stdout.write("Finished scraping.")