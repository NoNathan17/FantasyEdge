import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fantasy_football_assistant.settings')

app = Celery('fantasy_football_assistant')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
