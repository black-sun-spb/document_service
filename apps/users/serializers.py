from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации нового пользователя.

    Поля:
        email (str): Email пользователя.
        password (str): Пароль пользователя (только для записи).
        password2 (str): Подтверждение пароля (только для записи).

    Методы:
        validate(attrs): Проверяет совпадение паролей.
        create(validated_data): Создает нового пользователя с хешированным паролем.
    """

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "password", "password2")

    def validate(self, attrs):
        """
        Проверяет, что пароль и подтверждение совпадают.

        Args:
            attrs (dict): Данные сериализатора.

        Returns:
            dict: Данные сериализатора, если проверка прошла успешно.

        Raises:
            serializers.ValidationError: Если пароли не совпадают.
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords don't match."})
        return attrs

    def create(self, validated_data):
        """
        Создает нового пользователя с валидными данными.

        Args:
            validated_data (dict): Валидированные данные из сериализатора.

        Returns:
            User: Созданный пользователь.
        """
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
