from django.shortcuts import render

from .forms import FindForm
from .models import Development, Apartment


# Create your views here.

def home_view(request):
    development = request.GET.get('development')
    query_dev = Development.objects.all()
    query_set = []
    if development:
        _filter = {}
        _filter['development__name'] = development
        query_set = Apartment.objects.filter(**_filter)

    form = FindForm()
    return render(request, 'parsing/home.html', {'object_list': query_set,
                                                 'dev_list': query_dev,
                                                 'form': form})
