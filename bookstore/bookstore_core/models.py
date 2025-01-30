from django.db import models

# Create your models here.

# Publisher Model:
# Since the publisher is tied to each book, a separate model makes sense.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    

# Basic Book Information Model:
# This should hold essential information that is common across all books.

class Book(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    published_date = models.DateField()
    language = models.CharField(max_length= 50)
    summary = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Many-to-Many relationship with authors and categories
    authors = models.ManyToManyField('Author', blank=True)
    categories = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.title


# Author Model:
# Let’s assume that books can have multiple authors, so this model will allow for flexibility.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# Category Model
# Books may belong to multiple categories so using a Many-to-Many relationship makes sense here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


# Inventory Management
# Next, let's add an inventory system that tracks the stock levels and condition of each book.

class BookInventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField(default=0)
    condition = models.CharField(max_length=50, choices=[('new','New'),('used','Used')], default = 'new')


    def __str__(self):
        return f'{self.book.title} - {self.condition}'
    


# Adding Features Like Reviews, Ratings, and Sales Later
# As your system grows, you can introduce more specialized models like Review, Sale, and Rating when required.

# For instance, the Review model could look like this:

# class Review(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete= models.CASCADE)
#     rating = models.DecimalField(max_digits=3, decimal_places=2)
#     review_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Review for {self.book.title} by {self.user.username}'