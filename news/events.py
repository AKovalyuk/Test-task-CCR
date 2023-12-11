from constance.signals import config_updated
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, PeriodicTasks


@receiver(config_updated)
def constance_updated(**kwargs):
    key = kwargs['key']

    if key != 'NOTIFICATION_TIME':
        return

    new_time = kwargs['new_value']
    task = PeriodicTask.objects.get(
        task='send_email'
    )

    task.crontab.minute = new_time.minute
    task.crontab.hour = new_time.hour
    task.crontab.save()

    task.save()
    PeriodicTasks.changed(task)
