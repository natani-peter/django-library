from django.urls import path

from base import views

app_name = 'base'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('books/<int:pk>', views.about_book_page, name='about_book'),
    path('books/add-review/<int:pk>', views.add_book_review, name='book_review'),
    path('books/borrow/<int:pk>', views.borrow_book, name='borrow_book'),
    path('books/status/<int:pk>/', views.collect_status, name='collect_status'),
    path('books/return/<int:pk>/', views.return_book, name='return_book'),
    path('authors/', views.author, name='authors'),
    path('authors/<int:pk>', views.authorDetails, name='author'),
]
