from django.contrib import admin
from .models import Apartment, Development, Site

# Register your models here.

admin.site.register(Apartment)
admin.site.register(Development)
admin.site.register(Site)