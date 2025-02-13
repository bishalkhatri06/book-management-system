from django import forms
from .models import Book, Publisher, Author, Category, BookInventory

# modelform for Publisher   
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        # fields = ['name', 'address', 'contact']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),  # adding css class to the input field
            'address': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}) ,  # adding css class to the textarea field
            'contact': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),  # adding css class to the input field
        }


# model for create new author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'email': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'bio': forms.Textarea(attrs={'class': 'w-full p-2 border rounded'}),
        }   

# model for create new category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
    
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        }   

# model for create new book inventory
class BookInventoryForm(forms.ModelForm):
    class Meta:
        model = BookInventory
        fields = ['book', 'stock_quantity', 'condition']

        widgets = {
            'book': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'condition': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }

# model for create new book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'ISBN', 'publisher', 'published_date', 'language', 'summary', 'price', 'is_available', 'authors', 'categories']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),

            'ISBN': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'publisher': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'published_date': forms.DateInput(attrs={'class': 'w-full p-2 border rounded'}),
            'language': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'summary': forms.Textarea(attrs={'class': 'w-full p-2 border rounded'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'w-full p-2 border rounded'}),
            'authors': forms.SelectMultiple(attrs={'class': 'w-full p-2 border rounded'}),
            'categories': forms.SelectMultiple(attrs={'class': 'w-full p-2 border rounded'}),
        }

