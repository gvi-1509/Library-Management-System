from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Borrower, Accountant
from .serializers import BookSerializer, BorrowerSerializer, AccountantSerializer


class AccountantListCreateView(generics.ListCreateAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
   

class AccountantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantSerializer
  

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
  

class BorrowerListCreateView(generics.ListCreateAPIView):
    queryset = Borrower.objects.filter(returned=False)
    serializer_class = BorrowerSerializer
   

class BorrowerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
   

@api_view(['POST'])

def borrow_book(request, book_id, user_id):
    try:
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
        
        if book.available_stock > 0:
            Borrower.objects.create(user=user, book=book)
            book.available_stock -= 1
            book.save()
            return Response({"message": f"{user.username} borrowed {book.title}."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No copies available."}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])

def return_book(request, book_id, user_id):
    try:
        book = Book.objects.get(id=book_id)
        borrower = Borrower.objects.filter(book=book, user_id=user_id, returned=False).first()
        
        if borrower:
            borrower.returned = True
            borrower.save()
            book.available_stock += 1
            book.save()
            return Response({"message": f"Book {book.title} returned."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Borrower record not found or already returned."}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
