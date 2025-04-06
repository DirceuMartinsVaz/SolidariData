from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(request, 'landing_page/landing_page.html')

def home(request):
    return render(request, 'sdata/home.html')

def families(request):
    return render(request, 'sdata/families/families.html')

def events(request):
    return render(request, 'sdata/events/events.html')

def institutions(request):
    return render(request, 'sdata/institutions/institutions.html')