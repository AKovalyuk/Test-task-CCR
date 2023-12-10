import os
from datetime import timedelta

from celery import Celery
from constance import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_email_task': {
        'task': 'send_email',
        'schedule': timedelta(seconds=5),
    },
    'weather_task': {
        'task': 'weather_task',
        'schedule': timedelta(minutes=1),
    }
}
