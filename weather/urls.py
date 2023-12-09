from django.urls import path

from .views import PlaceViewSet


urlpatterns = [
    path('place/', PlaceViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('place/<int:pk>/', PlaceViewSet.as_view(
        {'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}
    )),
]
