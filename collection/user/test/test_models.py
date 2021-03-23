from datetime import datetime

from django.test import TestCase

from collection.user.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User(username='admin')
        self.user.set_password('admin123')
        self.user.save()

    def test_create(self):
        self.assertTrue(User.objects.exists())

    def test_str(self):
        self.assertEquals(str(self.user), 'admin')

    def test_username(self):
        self.assertEquals(self.user.username, 'admin')

    def test_created_at(self):
        self.assertIsInstance(self.user.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.user.modified_at, datetime)

    def test_name_can_not_be_blank_and_null(self):
        field = User._meta.get_field('username')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_check_pass(self):
        password = 'admin123'
        self.assertTrue(self.user.check_password(password))

    def test_check_pass_wrong(self):
        password = 'Admin321'
        self.assertFalse(self.user.check_password(password))

    def test_default_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_default_is_superuser(self):
        self.assertFalse(self.user.is_superuser)
