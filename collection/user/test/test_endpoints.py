from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from collection.user.serializers import (
    UpdateUserSerializer, User, UserSerializer
)
from collection.user.views import UserViewSet

factory = APIRequestFactory()


class UserTestViewSet(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin')
        self.user.set_password('admin123')
        self.user.is_superuser = True
        self.user.save()

    def test_create(self):
        data = {
            'username': 'ademir', 'email': 'admin@admin.com',
            'password1': 'admin4312', 'password2': 'admin4312'
        }
        request = factory.post('api/v1/user/', data)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_pass_not_equals(self):
        data = {
            'username': 'ademir', 'password1': '321admin',
            'password2': '321amin'
        }
        request = factory.post('api/v1/user/', data)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(
            dict(response.data)['password1'][0], 'As senhas não conferem'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all(self):
        request = factory.get('api/v1/user/')
        force_authenticate(request, user=self.user)
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        users = User.objects.filter(id=self.user.id).order_by('created_at')
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        request = factory.get('api/v1/user/',)
        force_authenticate(request, user=self.user)
        view = UserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.user.id)
        user = User.objects.get(pk=self.user.id)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update(self):
        data = {
            'username': 'ademir', 'email': 'admin@admin.com',
        }
        request = factory.post('api/v1/user/', data)
        force_authenticate(request, user=self.user)
        view = UserViewSet.as_view({'post': 'update'})
        response = view(request, pk=self.user.id)
        user = User.objects.get(pk=self.user.id)
        serializer = UpdateUserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = factory.delete('api/user/')
        force_authenticate(request, user=self.user)
        view = UserViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
