from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from collection.book.serializers import (
    Book, BookSerializer, Category, CategorySerializer
)
from collection.book.views import BookViewSet, CategoryViewSet
from collection.user.models import User

factory = APIRequestFactory()


class CategoryTestViewSet(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin123'
        )
        self.user.save()

        self.category = Category.objects.create(name='Teste')
        self.category.save()

    def test_create(self):
        data = {
            'name': 'Romance'
        }
        request = factory.post('api/v1/category/', data)
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        request = factory.get('api/v1/category/')
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'get': 'list'})
        response = view(request)
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category(self):
        request = factory.get('api/v1/category/',)
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.category.id)
        category = Category.objects.get(pk=self.category.pk)
        serializer = CategorySerializer(category)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update(self):
        data = {
            'name': 'Terror'
        }
        request = factory.post('api/v1/category/', data)
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({'post': 'update'})
        response = view(request, pk=self.category.id)
        category = Category.objects.get(pk=self.category.pk)
        serializer = CategorySerializer(category)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = factory.delete('api/category/')
        force_authenticate(request, user=self.user)
        view = CategoryViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=self.category.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookTestViewSet(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', password='admin123'
        )
        self.user.save()

        self.category = Category.objects.create(name='Teste')
        self.category.save()

        self.book = Book.objects.create(
            title='teste', author='guilherme', number_of_pages=45,
            category=self.category, user=self.user
        )
        self.book.save()

    def test_create(self):
        data = {
            'title': 'livro', 'author': 'guilherme', 'number_of_pages': 45,
            'category': self.category.pk, 'user': self.user.pk
        }
        request = factory.post('api/v1/book/', data)
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        request = factory.get('api/v1/book/')
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'get': 'list'})
        response = view(request)
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book(self):
        request = factory.get('api/v1/book/',)
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.book.id)
        book = Book.objects.get(pk=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update(self):
        data = {
            'title': 'livro2', 'author': 'guilherme', 'number_of_pages': 45,
            'category': self.category.pk, 'user': self.user.pk
        }
        request = factory.post('api/v1/book/', data)
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({'post': 'update'})
        response = view(request, pk=self.book.id)
        book = Book.objects.get(pk=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = factory.delete('api/book/')
        force_authenticate(request, user=self.user)
        view = BookViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
