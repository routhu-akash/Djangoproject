from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # or whatever your success URL is
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'form': form, 'books': books})


from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")
