from django.http import HttpResponse
from django.shortcuts import render
from .models import Hobby, Portfolio

def home(request):
    return render(request, "home.html")

def hobbies(request):
    hobbies = Hobby.objects.all()
    return render(request, "hobbies.html", {"hobbies": hobbies})

def portfolio(request):
    projects = Portfolio.objects.all()
    return render(request, "portfolio.html", {"projects": projects})

def contact(request):
    return render(request, "contact.html")