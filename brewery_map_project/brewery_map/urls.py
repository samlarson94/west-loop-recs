from django.urls import path
from . import views

urlpatterns = [
    path('', views.brewery_map, name='brewery_map'),
    path('get_directions/<str:address>/', views.get_directions, name='get_directions'),

]