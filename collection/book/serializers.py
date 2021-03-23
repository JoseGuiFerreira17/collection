from rest_framework import serializers

from collection.book.models import Book, Category


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        ordering = ['created_at']
        fields = [
            'id', 'title', 'author', 'number_of_pages', 'category', 'user',
            'created_at', 'modified_at'
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'created_at': {'read_only': True},
            'modified_at': {'read_only': True},
        }


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        ordering = ['created_at']
        fields = [
            'id', 'name', 'created_at', 'modified_at'
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'created_at': {'read_only': True},
            'modified_at': {'read_only': True},
        }
