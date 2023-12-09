from django.db import models
from django.contrib.auth.models import User


PREVIEW_MAX_SIDE = 200


class Post(models.Model):
    title = models.CharField(max_length=256)
    main_image = models.ImageField(upload_to='images')
    preview_image = models.ImageField(upload_to='previews', null=True, blank=True)
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
