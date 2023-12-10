from django.contrib import admin
from django.db.models.functions import TruncDate

from .models import Place, WeatherReport


class PlaceListFilter(admin.SimpleListFilter):
    title = "Place Filter"
    parameter_name = "place"

    def lookups(self, request, model_admin):
        return [
            (place.name, place.name) for place in
            Place.objects.all().distinct('name').only('name')[:15]
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        place_name = self.value()
        return queryset.filter(place__name=place_name)


class WeatherReportListFilter(admin.SimpleListFilter):
    title = "Date Filter"
    parameter_name = "timestamp"

    def lookups(self, request, model_admin):
        return [
            (str(date.date), str(date.date)) for date in
            WeatherReport.objects.annotate(date=TruncDate('timestamp')).distinct('date')[:15]
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(timestamp__date=self.value())
