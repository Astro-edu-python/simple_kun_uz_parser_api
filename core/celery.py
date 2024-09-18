import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

app = Celery('kun_uz_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'parse-news-periodic': {
        'task': 'apps.api.v1.main.tasks.parse_news_task_beat',
        'schedule': crontab(minute='*/60'),
    },
}

app.autodiscover_tasks()
