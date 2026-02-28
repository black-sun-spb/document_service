from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Кастомная админка для модели User без поля username.

    Переопределяет стандартный UserAdmin для корректного отображения
    и управления пользователями в админке Django, когда используется
    email как уникальный идентификатор.

    Атрибуты:
        list_display (tuple): Поля, отображаемые в списке пользователей.
        list_filter (tuple): Фильтры в правой панели админки.
        search_fields (tuple): Поля, доступные для поиска.
        ordering (tuple): Порядок сортировки в списке.
        fieldsets (tuple): Поля, отображаемые при редактировании пользователя.
        add_fieldsets (tuple): Поля, отображаемые при добавлении нового пользователя.
    """

    # Поля для отображения в списке пользователей
    list_display = ("id", "email", "is_staff", "is_active")

    # Фильтры по статусу админа и активности
    list_filter = ("is_staff", "is_active")

    # Поля для поиска (tuple должен содержать элементы)
    search_fields = ("email",)

    # Порядок сортировки
    ordering = ("id",)

    # Поля для редактирования пользователя
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Поля для добавления нового пользователя
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
