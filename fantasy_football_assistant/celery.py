from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fantasy_football_assistant.settings')

app = Celery('fantasy_football_assistant')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'scrape-news-every-minute': {
        'task': 'news.tasks.scrape_news_task',  # Replace with your actual task name
        'schedule': 60.0,  # 60 seconds
    },
}

