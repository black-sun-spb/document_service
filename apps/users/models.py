"""
Модель пользователя и менеджер пользователей.

Используется кастомная модель пользователя без username.
Аутентификация и создание пользователей происходит по email.
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Кастомный менеджер пользователей.

    Переопределяет стандартные методы Django, чтобы:
    - создавать обычных пользователей по email
    - создавать суперпользователей без username
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Создаёт и сохраняет обычного пользователя.

        :param email: Email пользователя (обязателен)
        :param password: Пароль пользователя
        :param extra_fields: Дополнительные поля модели
        :return: Экземпляр User
        """
        if not email:
            raise ValueError("Email обязателен для создания пользователя")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создаёт и сохраняет суперпользователя.

        Автоматически выставляет:
        - is_staff = True
        - is_superuser = True

        :param email: Email администратора
        :param password: Пароль администратора
        :param extra_fields: Дополнительные поля модели
        :return: Экземпляр User с правами администратора
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Кастомная модель пользователя.

    Особенности:
    - username полностью отключён
    - email используется как основной идентификатор
    """

    username = None  # Отключаем стандартное поле username
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """
        Строковое представление пользователя.
        Используется в админке и логах.
        """
        return self.email
