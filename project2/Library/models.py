from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter

class Accountant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    total_stock = models.IntegerField(default=0)  # Total books available in library
    available_stock = models.IntegerField(default=0)  # Number of books available for borrowing

    def __str__(self):
        return self.title


class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateField(auto_now_add=True)
    returned = models.BooleanField(default=False)  # ✅ Ensure this field exists

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
