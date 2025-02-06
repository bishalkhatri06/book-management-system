from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_add, name = 'book_add'),
    path('detail/<int:pk>/', views.book_detail, name = 'book_detail'),  # <int:pk> is used to capture the id of the book

    # Publishers
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/add/', views.publisher_add, name='publisher_add'),

    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_add, name='author_add'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
]