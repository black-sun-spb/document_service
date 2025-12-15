import os
from celery import Celery
from dotenv import load_dotenv
from pathlib import Path

# Задаем базовую директорию проекта и загружаем переменные окружения из .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Устанавливаем модуль настроек Django по умолчанию для Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Инициализация Celery
app = Celery("config")
"""
Создаем объект Celery для проекта Django.

Аргументы:
- "config": имя текущего проекта (используется для именования приложения Celery).
"""

# Загружаем конфигурацию из настроек Django с префиксом CELERY
app.config_from_object("django.conf:settings", namespace="CELERY")
"""
Подключение настроек Celery из Django settings.
Используем префикс CELERY для всех настроек Celery в settings.py
"""

# Автоматический поиск и регистрация задач (tasks.py) во всех приложениях Django
app.autodiscover_tasks()
"""
Celery автоматически ищет tasks.py во всех установленных приложениях (INSTALLED_APPS)
и регистрирует найденные задачи.
"""
