from django.db import models

# Create your models here.
class Brewery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    current_hours = models.CharField(max_length=100)
    full_hours = models.CharField(max_length=200)

    def __str__(self):
        return self.name