from django.contrib import admin
from django.core.files.base import ContentFile

from .models import Post
from utils import rescale


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'main_image',
        'preview_image',
        'text',
        'publish_date',
        'author',
    ]
    readonly_fields = ['preview_image']

    def save_model(self, request, obj: Post, form, change):
        obj.preview_image.save(
            name=obj.main_image.name,
            content=rescale(obj.main_image, 200),
        )
        super().save_model(request, obj, form, change)
