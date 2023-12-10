from rest_framework import viewsets, permissions, mixins, generics

from .models import Place, WeatherReport
from .serializers import PlaceSerializer, WeatherReportSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WeatherReportViewSet(viewsets.ModelViewSet):
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer
