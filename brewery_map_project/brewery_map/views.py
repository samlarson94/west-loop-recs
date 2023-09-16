from django.shortcuts import render
from django.shortcuts import render
from .models import Brewery
from brewery_map_project import config

def brewery_map(request):
    breweries = Brewery.objects.all()
    print(breweries, type(breweries))
    context = {
        'breweries': breweries,
        'api_key': config.API_KEY
    }
    return render(request, 'brewery_map/brewery_map.html', context)

