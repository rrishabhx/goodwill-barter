from django.shortcuts import render
from .models import Product


def home(request):
    context = {
        'goods': ['Home page'],
    }
    return render(request, 'products/home.html', context)


def productshome(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/productshome.html', context)


def serviceshome(request):
    context = {
        'goods': ['Services page'],
    }
    return render(request, 'products/serviceshome.html', context)
