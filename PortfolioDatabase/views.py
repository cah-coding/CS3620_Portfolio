from django.http import HttpResponse
from .models import Hobby
from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from .forms import PortfolioForm, ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")  # redirect or success page
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

@login_required
def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # redirect to your portfolio page
    else:
        form = PortfolioForm()
    return render(request, 'add_portfolio.html', {'form': form})

@login_required
def edit_portfolio(request, pk):
    item = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # back to homepage
    else:
        form = PortfolioForm(instance=item)
    return render(request, 'edit_portfolio.html', {'form': form, 'item': item})

@login_required
def delete_portfolio(request, pk):
    item = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('portfolio')  # back to homepage
    return render(request, 'confirm_delete.html', {'item': item})