from django.shortcuts import render


def home(request):
    context = {
        'goods': ['Harry Potter and the Sorcerer\'s Stone', 'Silence of the lambs'],
    }
    return render(request, 'products/home.html', context)
