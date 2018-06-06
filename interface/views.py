from django.shortcuts import render

def index(request):
    return render(request, 'interface/index.html')

def login(request):
    return render(request, 'interface/login.html')