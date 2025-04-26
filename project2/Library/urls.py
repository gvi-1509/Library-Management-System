from django.urls import path
from .views import (
    AccountantListCreateView, AccountantDetailView,
    BookListCreateView, BookDetailView,
    BorrowerListCreateView, BorrowerDetailView,
    borrow_book, return_book
)

urlpatterns = [
     # Accountant APIs
    path('accountants/', AccountantListCreateView.as_view(), name='accountant-list'),
    path('accountants/<int:pk>/', AccountantDetailView.as_view(), name='accountant-detail'),

    # Book APIs
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Borrower APIs
    path('borrowers/', BorrowerListCreateView.as_view(), name='borrower-list'),
    path('borrowers/<int:pk>/', BorrowerDetailView.as_view(), name='borrower-detail'),

    # Borrow and Return Book APIs
    path('borrow/<int:book_id>/<int:user_id>/', borrow_book, name='borrow-book'),
    path('return/<int:book_id>/<int:user_id>/', return_book, name='return-book'),
]



