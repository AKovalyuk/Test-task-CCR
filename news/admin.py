from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post
from utils import rescale


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = [
        'title',
        'main_image',
        'preview_image',
        'text',
        'publish_date',
        'author',
    ]
    readonly_fields = ['preview_image']
    summernote_fields = ['text']

    def save_model(self, request, obj: Post, form, change):
        obj.preview_image.save(
            name=obj.main_image.name,
            content=rescale(obj.main_image, 200),
        )
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
