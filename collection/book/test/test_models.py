from datetime import datetime
from model_mommy import mommy

from django.test import TestCase

from collection.book.models import Book, Category
from collection.user.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category(name='romance')
        self.category.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEquals(str(self.category), 'romance')

    def test_name(self):
        self.assertEquals(self.category.name, 'romance')

    def test_created_at(self):
        self.assertIsInstance(self.category.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.category.modified_at, datetime)

    def test_name_can_not_be_blank_and_null(self):
        field = Category._meta.get_field('name')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)


class BookModelTest(TestCase):
    def setUp(self):
        self.category = mommy.make(Category)
        self.user = mommy.make(User)
        self.book = Book(
            title='livro1', author='guilherme', number_of_pages=451,
            category=self.category, user=self.user
        )
        self.book.save()
    
    def test_create(self):
        self.assertTrue(Book.objects.exists())

    def test_str(self):
        self.assertEquals(str(self.book), 'livro1')

    def test_title(self):
        self.assertEquals(self.book.title, 'livro1')
    
    def test_author(self):
        self.assertEquals(self.book.author, 'guilherme')
    
    def test_number_of_pages(self):
        self.assertEquals(self.book.number_of_pages, 451)

    def test_created_at(self):
        self.assertIsInstance(self.book.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.book.modified_at, datetime)

    def test_title_can_not_be_blank_and_null(self):
        field = Book._meta.get_field('title')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
           
    def test_author_can_not_be_blank_and_null(self):
        field = Book._meta.get_field('author')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_number_of_pages_can_not_be_blank_and_null(self):
        field = Book._meta.get_field('number_of_pages')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_category_can_not_be_blank_and_null(self):
        field = Book._meta.get_field('category')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_user_can_not_be_blank_and_null(self):
        field = Book._meta.get_field('user')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)
