from django.shortcuts import render, redirect

# importing models from models.py
from .models import Book
from .models import Publisher
from .models import Author
from .models import Category

# importing forms from forms.py
from .forms import BookForm
from .forms import PublisherForm
from .forms import AuthorForm
from .forms import CategoryForm


# Create your views here.

# creating a view to list publishers
def publisher_list(request):
    publishers = Publisher.objects.all() # querying all books from the database
    return render(request, 'books/publisher_list.html', {'publishers': publishers})

# creating a view to add a new publisher
def publisher_add(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()  # save the new publisher to the database
            return redirect('publisher_list')  # redirect to the list of publishers
    
    else:
        form = PublisherForm()

    return render(request, 'books/publisher_add.html', {'form': form})

# creating a view to edit a publisher
def publisher_edit(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'books/publisher_edit.html', {'form': form, 'publisher': publisher})

# creating a view to delete a publisher
def publisher_delete(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'books/publisher_delete.html', {'publisher': publisher})

# creating a view to list authors
def author_list(request):
    authors = Author.objects.all() # querying all books from the database
    return render(request, 'books/author_list.html', {'authors': authors})

# creating a view to add a new author
def author_add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()  # save the new author to the database
            return redirect('author_list')  # redirect to the list of authors
    
    else:
        form = AuthorForm()

    return render(request, 'books/author_add.html', {'form': form})

# creating a view to edit an author
def author_edit(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/author_edit.html', {'form': form, 'author': author})

# creating a view to delete an author
def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'books/author_delete.html', {'author': author})


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

