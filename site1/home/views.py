from django.shortcuts import render

def get_home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'home.html')

def challenge(request):
    return render(request, 'home.html')
# Create your views here.
