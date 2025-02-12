from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.book_add, name = 'book_add'),
    path('detail/<int:pk>/', views.book_detail, name = 'book_detail'),  # <int:pk> is used to capture the id of the book

    # Publishers
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/add/', views.publisher_add, name='publisher_add'),
    path('publishers/edit/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/delete/<int:pk>/', views.publisher_delete, name='publisher_delete'),

    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_add, name='author_add'),
    path('authors/edit/<int:pk>/', views.author_edit, name='author_edit'),
    path('authors/delete/<int:pk>/', views.author_delete, name='author_delete'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
]