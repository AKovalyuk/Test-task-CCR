from django.contrib import admin
from django_admin_geomap import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Place, WeatherReport
from .filters import PlaceListFilter, WeatherReportListFilter


# Register your models here.
class Admin(ModelAdmin, ImportExportModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_item_zoom = "10"


class WeatherReportAdmin(admin.ModelAdmin):
    ordering = ["-timestamp",]
    list_filter = [PlaceListFilter, WeatherReportListFilter]


admin.site.register(Place, Admin)
admin.site.register(WeatherReport, WeatherReportAdmin)
