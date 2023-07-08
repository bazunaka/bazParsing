from django.db import models

# Create your models here.

class Apartment(models.Model):
    name = models.CharField(max_length=50)
    square = models.FloatField()
    price = models.IntegerField()
    date = models.DateField()
    decor = models.BooleanField()
    date_view = models.DateField()
    is_metro = models.BooleanField()
    metro_name = models.CharField(max_length=50, blank=True)
    is_mcd = models.BooleanField()
    mcd_name = models.CharField(max_length=50, blank=True)
    rent = models.IntegerField()
    mortgage = models.IntegerField()