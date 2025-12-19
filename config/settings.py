import os
from pathlib import Path
from dotenv import load_dotenv

# ----------------------------------------------------------------------
# Базовая директория проекта и загрузка переменных окружения
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))
"""
BASE_DIR: путь к корневой директории проекта.
load_dotenv(): загружает переменные окружения из .env файла.
"""

# ----------------------------------------------------------------------
# Основные настройки безопасности
# ----------------------------------------------------------------------
SECRET_KEY = "django-insecure-r#_1^+qbpdw4x+g)fodw!xc=(4@!-34(c-z($s+9n0l^&#jf=a"
"""
SECRET_KEY: секретный ключ для Django. Не использовать в продакшене публично.
"""

DEBUG = True
"""
DEBUG: включение/отключение режима отладки. В продакшене должно быть False.
"""

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
"""
ALLOWED_HOSTS: список разрешённых хостов для проекта.
"""

# ----------------------------------------------------------------------
# Установленные приложения
# ----------------------------------------------------------------------
INSTALLED_APPS = [
    "grappelli",  # UI для админки
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",  # Django REST Framework
    "rest_framework.authtoken",  # токены для API
    "drf_spectacular",  # документация API
    "apps.users",  # кастомное приложение пользователей
    "apps.documents",  # приложение документов
]
"""
INSTALLED_APPS: список приложений Django и сторонних пакетов.
"""

# ----------------------------------------------------------------------
# Middleware
# ----------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
"""
MIDDLEWARE: последовательность классов промежуточной обработки запросов.
"""

# ----------------------------------------------------------------------
# URL и шаблоны
# ----------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
"""
ROOT_URLCONF: основной модуль URLconf проекта.
"""

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # папки с кастомными шаблонами
        "APP_DIRS": True,  # использовать шаблоны приложений
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
"""
TEMPLATES: конфигурация шаблонов Django.
"""

WSGI_APPLICATION = "config.wsgi.application"
"""
WSGI_APPLICATION: точка входа WSGI для деплоя.
"""

# ----------------------------------------------------------------------
# Настройки базы данных
# ----------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}
"""
DATABASES: настройки подключения к PostgreSQL.
"""

# ----------------------------------------------------------------------
# Валидация паролей
# ----------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
"""
AUTH_PASSWORD_VALIDATORS: правила проверки паролей пользователей.
"""

# ----------------------------------------------------------------------
# Локализация
# ----------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
"""
Настройки языка, часового пояса и интернационализации.
"""

# ----------------------------------------------------------------------
# Кастомная модель пользователя
# ----------------------------------------------------------------------
AUTH_USER_MODEL = "users.User"
"""
AUTH_USER_MODEL: указывает на кастомную модель User.
"""

# ----------------------------------------------------------------------
# Django REST Framework
# ----------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
"""
REST_FRAMEWORK: настройки DRF, включая аутентификацию и права доступа.
"""

# ----------------------------------------------------------------------
# Медиа-файлы
# ----------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
"""
MEDIA_URL: URL для доступа к медиа-файлам.
MEDIA_ROOT: папка на диске для хранения загружаемых файлов.
"""

# ----------------------------------------------------------------------
# Email
# ----------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
"""
Настройки SMTP для отправки почты через Gmail.
"""

# ----------------------------------------------------------------------
# Celery
# ----------------------------------------------------------------------
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
"""
CELERY_BROKER_URL: брокер сообщений (Redis).
CELERY_RESULT_BACKEND: бэкенд результатов задач Celery.
"""

# ----------------------------------------------------------------------
# DRF Spectacular (OpenAPI / Swagger)
# ----------------------------------------------------------------------
SPECTACULAR_SETTINGS = {
    "TITLE": "Document Service API",
    "DESCRIPTION": "API для загрузки документов и уведомлений",
    "VERSION": "1.0.0",
}
"""
SPECTACULAR_SETTINGS: настройки генерации документации API.
"""

# ----------------------------------------------------------------------
# Статические файлы
# ----------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
"""
STATIC_URL: URL для доступа к статическим файлам.
STATIC_ROOT: папка, куда собираются статические файлы командой collectstatic.
"""
