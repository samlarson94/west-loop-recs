from django.shortcuts import render, redirect
from .models import Brewery
from brewery_map_project import config
from django.http import HttpResponse
from urllib.parse import quote_plus

def brewery_map(request):
    # Sort by Elisa Rating Score
    breweries = Brewery.objects.all().order_by('-e_rating')

    context = {
        'breweries': breweries,
        'api_key': config.GOOGLE_API_KEY
    }
    return render(request, 'brewery_map/brewery_map.html', context)

def get_directions(request, address):
    encoded_address = quote_plus(address)

    if encoded_address:
        # Redirect the user to Google Maps with directions
        google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={encoded_address}"
        return redirect(google_maps_url)
    else:
        return HttpResponse("Address Not Found")