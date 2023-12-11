from datetime import datetime

from django.core.mail import send_mail
from constance import config
from django.contrib.auth.models import User

from core.celery import app
from core import settings
from .models import Post


@app.task(name='send_email')
def send_email():
    if settings.EMAIL_HOST_USER == '...':
        return
    today_posts = Post.objects.filter(publish_date__date__gte=datetime.now().date())[:15]
    emails = (User.objects
              .filter(email__isnull=False)
              .values_list('email', flat=True))
    send_mail(
        subject=config.DAILY_MAIL_TITLE,
        message='\n'.join(post.title for post in today_posts),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=True,
    )
