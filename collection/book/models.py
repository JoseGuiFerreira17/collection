import uuid
from django.db import models


class Category(models.Model):
    id = models.UUIDField(
        verbose_name='ID da categoria', primary_key=True,
        default=uuid.uuid4, editable=False
    )
    name = models.CharField('nome', max_length=255)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Book(models.Model):
    id = models.UUIDField(
        verbose_name='ID do livro', primary_key=True,
        default=uuid.uuid4, editable=False
    )
    title = models.CharField('titulo', max_length=255)
    author = models.CharField('autor', max_length=255)
    number_of_pages = models.PositiveIntegerField('numero de paginas')
    category = models.ForeignKey(
        'book.Category', on_delete=models.PROTECT,
        verbose_name='categoria', related_name='book_category_relation',
    )
    user = models.ForeignKey(
        'user.User', on_delete=models.PROTECT,
        verbose_name='usuario', related_name='book_user_relation',
        blank=True, null=True
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'