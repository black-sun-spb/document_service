from django.test import TestCase
from apps.users.serializers import RegisterSerializer


class RegisterSerializerTests(TestCase):
    """
    Тесты для сериализатора регистрации пользователей по email и паролю.
    """

    def test_valid_data_creates_user(self):
        """
        Проверяет, что сериализатор с корректными данными создаёт пользователя.
        """
        data = {
            "email": "newuser@example.com",
            "password": "StrongPassword123",
            "password2": "StrongPassword123",
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.email, "newuser@example.com")
        self.assertTrue(user.check_password("StrongPassword123"))

    def test_passwords_must_match(self):
        """
        Проверяет, что сериализатор выдаёт ошибку, если пароли не совпадают.
        """
        data = {
            "email": "newuser@example.com",
            "password": "StrongPassword123",
            "password2": "WrongPassword123",
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_password_validation(self):
        """
        Проверяет, что сериализатор использует встроенные валидаторы пароля.
        """
        data = {
            "email": "newuser@example.com",
            "password": "123",  # слишком короткий/слабый пароль
            "password2": "123",
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
