from rest_framework import viewsets
from .models import BookData
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fiction')
    serializer_class = BookSerializer

class ScienceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Science')
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='History')
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Biography')
    serializer_class = BookSerializer

class MysteryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Mystery')
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Horror')
    serializer_class = BookSerializer

class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Poetry')
    serializer_class = BookSerializer

class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Adventure')
    serializer_class = BookSerializer