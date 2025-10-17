from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/", views.home, name="home"),             # homepage
    path("hobbies/", views.hobbies, name="hobbies"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("hobbies/<int:hobby_id>/", views.hobby_detail, name="hobby_detail"),
    path("portfolio/<int:portfolio_id>/", views.portfolio_detail, name="portfolio_detail"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('portfolio/add/', views.add_portfolio, name='add_portfolio'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='portfolio_list'), name='logout'),
    path('portfolio/<int:pk>/edit/', views.edit_portfolio, name='edit_portfolio'),
    path('portfolio/<int:pk>/delete/', views.delete_portfolio, name='delete_portfolio'),
]