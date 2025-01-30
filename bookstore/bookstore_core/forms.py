from django import forms
from .models import Book


# model for create new book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','ISBN','publisher','price','authors','categories']

    