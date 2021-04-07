from django.shortcuts import render


def welcome(request):
    context = {
        'goods': ['Hello, Welcome'],
    }
    return render(request, 'products/welcome.html', context)

def home(request):
    context = {
        'goods': ['Home page'],
    }
    return render(request, 'products/home.html', context)

def productshome(request):
    context = {
        'goods': ['Products page'],
    }
    return render(request, 'products/productshome.html', context)

def serviceshome(request):
    context = {
        'goods': ['Services page'],
    }
    return render(request, 'products/serviceshome.html', context)