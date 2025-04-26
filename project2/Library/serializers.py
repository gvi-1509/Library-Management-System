from rest_framework import serializers
from .models import Book, Borrower, Accountant

class AccountantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountant
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    borrowed_at = serializers.DateField()

    class Meta:
        model = Borrower
        fields = '__all__'