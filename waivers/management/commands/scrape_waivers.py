from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from rankings.models import Waiver

def scrape_wauvers() -> list[dict]:
    pass