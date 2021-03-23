from rest_framework.viewsets import ModelViewSet

from collection.user.models import User
from collection.user.permissions import IsAuthenticatedOrWriteOnly
from collection.user.serializers import (UserSerializer, UpdateUserSerializer)


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrWriteOnly]
    filter_fields = ('username')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('created_at')
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateUserSerializer
        return UserSerializer

    
