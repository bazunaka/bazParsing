from django.shortcuts import render
from .models import Development, Apartment


# Create your views here.

def home_view(request):
    query_set = Apartment.objects.all()
    return render(request, 'parsing/home.html', {'object_list': query_set})
