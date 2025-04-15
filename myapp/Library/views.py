# In your views.py file
from django.shortcuts import render
from .models import Book  # Adjust if necessary

def book_list(request):
    books = Book.objects.all()  # Example of fetching all books
    return render(request, 'book_list.html', {'books': books})
