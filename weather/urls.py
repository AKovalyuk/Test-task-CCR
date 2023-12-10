from django.urls import path

from .views import PlaceViewSet, WeatherReportViewSet


urlpatterns = [
    path('place/', PlaceViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('place/<int:pk>/', PlaceViewSet.as_view(
        {'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}
    )),
    path('weather_report/', WeatherReportViewSet.as_view(
        {'get': 'list'}
    )),
    path('weather_report/<int:pk>/', WeatherReportViewSet.as_view(
        {'get': 'retrieve'}
    )),
]
