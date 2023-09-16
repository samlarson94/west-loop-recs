from django.urls import path
from . import views

urlpatterns = [
    path('', views.brewery_map, name='brewery_map'),
]