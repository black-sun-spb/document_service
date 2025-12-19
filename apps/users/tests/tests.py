from django.test import TestCase
from apps.users.models import User


class UserModelTests(TestCase):
    """
    Тесты модели пользователя.

    Проверяет создание обычного пользователя и суперпользователя
    с учетом кастомной модели User без поля username.
    """

    def test_create_user(self):
        """
        Проверяет создание пользователя с корректными данными.
        """
        user = User.objects.create_user(
            email="testuser@example.com",
            password="strongpassword123",
        )
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("strongpassword123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Проверяет создание суперпользователя.
        """
        admin = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword123"
        )
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
        self.assertEqual(admin.email, "admin@example.com")
