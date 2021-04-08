from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


def home(request):
    #we are not using context
    context = {
        'goods': ['Home page'],
    }
    return render(request, 'products/home.html', context)


def productshome(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/productshome.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/productshome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'products'
    ordering = ['-date_posted']


class ProductDetailView(DetailView):
    model = Product


def serviceshome(request):
    context = {
        'goods': ['Services page'],
    }
    return render(request, 'products/serviceshome.html', context)
