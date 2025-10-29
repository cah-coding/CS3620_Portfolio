from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BookData

def book_list(request):
    q = request.GET.get('q', '').strip()
    books = BookData.objects.all().order_by('name')

    if q:
        books = books.filter(
            name__icontains=q
        ) | books.filter(
            category__icontains=q
        ) | books.filter(
            description__icontains=q
        )

    paginator = Paginator(books, 6)  # 5–10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': q,
    }
    return render(request, 'book/book_list.html', context)