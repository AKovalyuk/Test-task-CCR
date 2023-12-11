import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from constance import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_email_task': {
        'task': 'send_email',
        'schedule': crontab(
            hour=config.NOTIFICATION_TIME.hour,
            minute=config.NOTIFICATION_TIME.minute,
        ),
    },
    'weather_task': {
        'task': 'weather_task',
        'schedule': timedelta(minutes=config.WEATHER_CHECK_PERIOD_MINUTES),
    }
}
