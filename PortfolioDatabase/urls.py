from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),             # homepage
    path("hobbies/", views.hobbies, name="hobbies"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/<int:hobby_id>/", views.hobby_detail, name="hobby_detail"),
    path("portfolio/<int:portfolio_id>/", views.portfolio_detail, name="portfolio_detail"),
]