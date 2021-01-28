from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def quemsomos(request):
    return render(request, 'quemsomos.html', {})

def faleconosco(request):
    return render(request, 'faleconosco.html', {})

def sobre(request):
    return render(request, 'sobre.html', {})