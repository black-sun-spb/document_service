from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    """
    API view для регистрации нового пользователя.

    Атрибуты:
    - serializer_class: сериализатор, используемый для валидации и создания пользователя.
    - permission_classes: разрешение доступа; AllowAny позволяет любому пользователю обращаться к эндпоинту.

    POST-запрос:
    Ожидает данные:
        {
            "email": "string",
            "password": "string",
            "password2": "string"  # повтор пароля для проверки совпадения
        }

    Возвращает:
    - 201 Created при успешной регистрации с данными созданного пользователя (без пароля).
    - 400 Bad Request при ошибках валидации.
    """

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
