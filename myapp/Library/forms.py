from django import forms
from .models import BookRecord

class BookRecordForm(forms.ModelForm):
    class Meta:
        model = BookRecord
        fields = ['student_name', 'book_name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
