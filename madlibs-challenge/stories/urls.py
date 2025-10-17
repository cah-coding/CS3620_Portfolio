from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Homepage listing all stories
    path('story/<int:story_id>/', views.story_form, name='story_form'),
]