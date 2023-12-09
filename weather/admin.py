from django.contrib import admin
from django_admin_geomap import ModelAdmin

from .models import Place


# Register your models here.
class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_item_zoom = "10"


admin.site.register(Place, Admin)
