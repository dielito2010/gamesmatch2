from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'home.html')