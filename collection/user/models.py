import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from collection.user.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(
        verbose_name='ID', primary_key=True, default=uuid.uuid4,
        editable=False
    )
    username = models.CharField('nome', max_length=255, unique=True)
    email = models.EmailField('e-mail', blank=True, null=True)
    is_superuser = models.BooleanField('superuser', default=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
