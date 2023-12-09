from django.urls import path

from news import views

urlpatterns = [
    path('post/', views.PostViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('post/<int:pk>/', views.PostViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
]
