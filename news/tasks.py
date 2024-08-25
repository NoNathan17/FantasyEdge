# tasks.py
from celery import shared_task
from .management.commands.scrape_news import scrape_news

@shared_task
def scrape_news_task():
    scrape_news()
