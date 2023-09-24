from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, default="West Loop")
    address = models.CharField(max_length=200)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # current_hours = models.CharField(max_length=100)
    # full_hours = models.CharField(max_length=200)
    s_rating = models.DecimalField(max_digits=3, decimal_places=0, default=00)
    e_rating = models.DecimalField(max_digits=3, decimal_places=0, default=00)
    knownfor = models.CharField(max_length=100, default='unspecified')
    patio = models.BooleanField(default=False)
    yelp = models.URLField(max_length=200, default="https://www.yelp.com/")
    
    def __str__(self):
        return self.name