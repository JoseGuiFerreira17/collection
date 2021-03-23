from rest_framework.permissions import IsAuthenticated

from collection.book.serializers import (
    Book, BookSerializer, Category, CategorySerializer
)
from rest_framework.viewsets import ModelViewSet
from collection.user.models import User


class BookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    filterset_fields = (
        'title', 'author', 'number_of_pages', 'category', 'user'
    )
    ordering = ('-created_at')

    def get_queryset(self, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        if user.is_superuser:
            return Book.objects.all()
        return Book.objects.filter(user=user)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_fields = ('name',)
    ordering = ('-created_at')  
