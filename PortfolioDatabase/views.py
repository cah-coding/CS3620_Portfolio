from django.http import HttpResponse
from .models import Hobby
from django.shortcuts import render, get_object_or_404
from .models import Portfolio

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

def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, id=hobby_id)
    return render(request, "hobby_detail.html", {"hobby": hobby})

def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    return render(request, "portfolio_detail.html", {"portfolio": portfolio})