## Проект **Document Service** 
позволяет пользователям загружать документы и отслеживать их статус. Администраторы могут управлять документами через кастомную панель Django Admin с Grappelli и получать уведомления о новых документах.

## Особенности

- Регистрация и аутентификация пользователей (JWT и сессии)
- Загрузка документов с валидацией формата и размера
- Уведомления администратору о новых документах (Celery + SMTP)
- Изменение статуса документов с уведомлением пользователя
- Кастомная админка с Grappelli (улучшенный интерфейс)
- OpenAPI схема и Swagger UI для документации API
- Покрытие тестами > 90 %
- Docker‑контейнеризация для удобной разработки и деплоя
- Логирование действий пользователей и администраторов

## Стек технологий

- **Backend**: Python 3.13, Django 6, Django REST Framework
- **Брокер/очереди**: Celery + Redis
- **База данных**: PostgreSQL
- **Админка**: Grappelli (надстройка над Django Admin)
- **API**: drf‑spectacular (OpenAPI/Swagger)
- **Контейнеризация**: Docker & Docker Compose
- **Аутентификация**: djangorestframework‑simplejwt
- **Почта**: SMTP (настройка через \`.env\`)
- **Тестирование**: unittest, coverage.py

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone \<URL_REPO\>
cd document_service
```

### 2. Создание и активация виртуального окружения

```bash
python -m venv .venv
.\\\.venv\\Scripts\\activate  # Windows
source .venv/bin/activate    # Linux/macOS
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка окружения (\`.env\`)

Создайте файл \`.env\` в корне проекта и заполните:

```env
# База данных
POSTGRES_DB=document_service
POSTGRES_USER=docuser
POSTGRES_PASSWORD=your_secure_password
POSTGRES_HOST=db
POSTGRES_PORT=5432


# Почта (пример для Gmail)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

# Админ
ADMIN_EMAIL=admin@example.com


# Django
SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# JWT
JWT_SECRET_KEY=your_jwt_secret
```

> **Важно**: замените значения на свои. Для \`SECRET_KEY\` и \`JWT_SECRET_KEY\` используйте случайные строки.

### 5. Запуск через Docker (рекомендуется)

1. Соберите контейнеры:  
   ```bash
   docker-compose up -d --build
   ```

2. Примените миграции:  
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Создайте суперпользователя:  
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. Соберите статические файлы:  
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

### 6. Запуск без Docker (для разработки)

1. Запустите PostgreSQL локально (убедитесь, что сервер доступен на \`localhost:5432\`).  
2. Примените миграции:  
   ```bash
   python manage.py migrate
   ```
3. Создайте суперпользователя:  
   ```bash
   python manage.py createsuperuser
   ```
4. Запустите сервер:  
   ```bash
   python manage.py runserver
   ```

## Доступ к интерфейсам


- **Админка Django**: \`http://localhost:8000/admin/\`  
- **Swagger UI (API docs)**: \`http://localhost:8000/swagger/\`  
- **OpenAPI схема**: \`http://localhost:8000/api/schema/\`  


## Тестирование


1. Запуск тестов:  
   ```bash
   docker-compose exec web coverage run manage.py test
   ```

2. Просмотр отчёта о покрытии:  
   ```bash
   docker-compose exec web coverage report
   ```

3. Генерация HTML‑отчёта:  
   ```bash
   docker-compose exec web coverage html
   ```
   Отчёт будет в папке \`htmlcov/\`.

## Структура проекта

```
document_service/
├── apps/
│   ├── documents/          # Модуль документов
│   │   ├── models.py       # Модели (Document, Status)
│   │   ├── serializers.py  # Сериализаторы DRF
│   │   ├── views.py        # API-вью
│   │   ├── tasks.py        # Задачи Celery
│   │   ├── urls.py         # Эндпоинты API
│   │   └── tests/          # Тесты модуля
│   └── users/              # Модуль пользователей
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── tests/
├── config/                 # Настройки проекта
│   ├── settings.py         # Настройки Django
│   ├── celery.py           # Настройка Celery
│   └── urls.py             # Основные URL
├── static/                 # Статические файлы
├── templates/              # Шаблоны (если используются)
├── docker-compose.yml      # Конфигурация Docker
├── manage.py
├── requirements.txt        # Зависимости Python
├── .env                    # Переменные окружения
└── README.md
```

## Настройка Celery и Redis

1. Убедитесь, что Redis запущен (в Docker он стартует автоматически).  
2. Запустите worker Celery:  
   ```bash
   docker-compose exec web celery -A config worker -l info
   ```
3. Запустите beat для периодических задач:  
   ```bash
   docker-compose exec web celery -A config beat -l info
   ```

## Полезные команды

- **Миграции**: \`python manage.py makemigrations\`  
- **Применение миграций**: \`python manage.py migrate\`  
- **Создание суперпользователя**: \`python manage.py createsuperuser\`  
- **Сбор статических файлов**: \`python manage.py collectstatic\`  
- **Проверка покрытия тестами**: \`coverage run manage.py test && coverage report\`  

## Контакты

По вопросам и предложениям:  
- Email: \`taisiya199264@gmail.com\`  
- Issue tracker: \`https://github.com/black-sun-spb/document_service/issues/`  

## Лицензия

Проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE).
