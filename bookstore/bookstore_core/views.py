from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

# Creating a View to List Books
def book_list(request):
    books = Book.objects.all() # querying all books from the database
    return render(request, 'book_list.html',{'books': books})


# creating view to add a new book
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # save the new book to the database
            return redirect('book_list')  # redirect to the list of books
    
    else:
        form = BookForm()

    return render(request, 'book_add.html', {'form': form})

