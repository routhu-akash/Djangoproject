from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'publication', 'year']
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date'})
        }
