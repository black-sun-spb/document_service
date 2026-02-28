from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

"""
URL-конфигурация для приложения users.

Endpoints:

- /register/       : Регистрация нового пользователя.
- /token/          : Получение JWT токена (access и refresh).
- /token/refresh/  : Обновление access токена с помощью refresh токена.
"""

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
