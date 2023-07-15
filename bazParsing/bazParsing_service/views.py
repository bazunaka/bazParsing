from django.shortcuts import render
import datetime


def home_views(request):
    date = datetime.datetime.now().date()
    name = 'Test'
    _context = {'date': date, 'name': name}
    return render(request, 'base.html', _context)
