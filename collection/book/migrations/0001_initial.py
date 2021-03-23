# Generated by Django 2.2.16 on 2021-03-23 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID da categoria')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID do livro')),
                ('title', models.CharField(max_length=255, verbose_name='titulo')),
                ('author', models.CharField(max_length=255, verbose_name='autor')),
                ('number_of_pages', models.PositiveIntegerField(verbose_name='numero de paginas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_category_relation', to='book.Category', verbose_name='categoria')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book_user_relation', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'livro',
                'verbose_name_plural': 'livros',
            },
        ),
    ]