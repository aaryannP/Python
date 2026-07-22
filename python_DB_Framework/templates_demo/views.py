from django.shortcuts import render

def home(request):
    return render(request, 'templates_demo/home.html')

def explore(request):
    return render(request, 'templates_demo/explore.html')
