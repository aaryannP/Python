from django.shortcuts import render
import logging
from .models import Book

logger = logging.getLogger(__name__)

def home_view(request):
    logger.debug("Home view accessed.")
    return render(request, 'advanced_topics/home.html')

def book_list_view(request):
    # Using select_related to optimize DB query for the related Author object
    books = Book.objects.select_related('author').all()
    logger.debug(f"Fetched {books.count()} books using select_related.")
    return render(request, 'advanced_topics/book_list.html', {'books': books})
