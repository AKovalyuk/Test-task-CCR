from rest_framework import viewsets, permissions, decorators, throttling
from django.http import HttpResponse

from utils import export
from .models import Place, WeatherReport
from .serializers import PlaceSerializer, WeatherReportSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WeatherReportViewSet(viewsets.ModelViewSet):
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer


class ExportThrottle(throttling.UserRateThrottle):
    rate = '5/minute'


@decorators.api_view(['GET'])
@decorators.throttle_classes([ExportThrottle])
# pylint: disable=unused-argument
def export_xlsx(request):
    queryset = WeatherReport.objects.all()
    if request.query_params.get('place'):
        queryset = queryset.filter(place__name=request.query_params.get('place'))
    if request.query_params.get('date'):
        queryset = queryset.filter(timestamp__date=request.query_params.get('date'))
    buffer = export(queryset.values())
    response = HttpResponse(
        buffer.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=weather.xlsx'
    return response
