from django.shortcuts import render
from django.shortcuts import render
from .models import Brewery
from brewery_map_project import config

def brewery_map(request):
    # Sort by Elisa Rating Score
    breweries = Brewery.objects.all().order_by('-e_rating')

    context = {
        'breweries': breweries,
        'api_key': config.API_KEY
    }
    return render(request, 'brewery_map/brewery_map.html', context)

