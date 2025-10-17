from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('books', views.BookViewSet, basename='books')
router.register('fiction', views.FictionViewSet, basename='fiction')
router.register('science', views.ScienceViewSet, basename='science')
router.register('history', views.HistoryViewSet, basename='history')
router.register('fantasy', views.FantasyViewSet, basename='fantasy')
router.register('biography', views.BiographyViewSet, basename='biography')
router.register('mystery', views.MysteryViewSet, basename='mystery')
router.register('romance', views.RomanceViewSet, basename='romance')
router.register('horror', views.HorrorViewSet, basename='horror')
router.register('poetry', views.PoetryViewSet, basename='poetry')
router.register('adventure', views.AdventureViewSet, basename='adventure')

urlpatterns = [
    path('', include(router.urls)),
]