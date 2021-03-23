from django.contrib import admin
from collection.book.models import Book, Category


admin.site.register(Category)

admin.site.register(Book)
