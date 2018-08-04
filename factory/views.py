from django.shortcuts import render
from .models import City


# Create your views here.
def main(request):
    return render(request, 'factory/index.html')


def suppliers(request):
    return render(request, 'factory/suppliers.html', {
        'cities': City.objects.all().order_by('-name')
        })


def town(request, town):

    return render(request, 'factory/town.html', {
        'town': City.objects.get(id=town)
        })
