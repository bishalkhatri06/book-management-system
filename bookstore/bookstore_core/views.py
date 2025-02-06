from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

# creating a view to list publishers
def publisher_list(request):
    return render(request, 'books/publisher_list.html')

# creating a view to add a new publisher
def publisher_add(request):
    return render(request, 'books/publisher_add.html')

# creating a view to list authors
def author_list(request):
    return render(request, 'books/author_list.html')

# creating a view to add a new author
def author_add(request):
    return render(request, 'books/author_add.html')

# creating a view to list categories
def category_list(request):
    return render(request, 'books/category_list.html')

# creating a view to add a new category
def category_add(request):
    return render(request, 'books/category_add.html')

# Creating a View to List Books
def book_list(request):
    books = Book.objects.all() # querying all books from the database
    return render(request, 'books/book_list.html',{'books': books})


# creating view to add a new book
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # save the new book to the database
            return redirect('books/book_list')  # redirect to the list of books
    
    else:
        form = BookForm()

    return render(request, 'books/book_add.html', {'form': form})

# creating view detail of a book
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

