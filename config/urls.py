from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

"""
Главный URLconf проекта.

Здесь подключаются:
- админка Django и Grappelli,
- API (приложения users и documents),
- документация API через DRF Spectacular (OpenAPI / Swagger),
- корневая страница проекта,
- раздача медиа и статических файлов в режиме DEBUG.
"""


def index(request):
    """
    Корневая страница сервиса.

    Используется как landing-page проекта и точка проверки,
    что сервер и контейнеры запущены корректно.
    """
    return HttpResponse(
        "<h1>Document Service</h1>"
        "<p>Backend service is running.</p>"
        "<p>Swagger: <a href='/swagger/'>/swagger/</a></p>"
    )


urlpatterns = [
    # Корневая страница
    path("", index, name="index"),

    # Grappelli — расширенный интерфейс админки Django
    path("grappelli/", include("grappelli.urls")),

    # Стандартная админка Django
    path("admin/", admin.site.urls),

    # OpenAPI схема для автоматической генерации спецификации API
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI для интерактивной документации API
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),

    # REST API приложения users
    path("api/users/", include("apps.users.urls")),

    # REST API приложения documents
    path("api/documents/", include("apps.documents.urls")),
]

# ----------------------------------------------------------------------
# Раздача медиа-файлов в режиме разработки
# ----------------------------------------------------------------------
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
static(): добавляет обработку URL для медиа-файлов, чтобы Django мог отдавать
загруженные пользователями файлы в режиме DEBUG.
"""

# ----------------------------------------------------------------------
# Раздача статических файлов в режиме разработки
# ----------------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
В режиме DEBUG Django раздает статические файлы (CSS, JS, изображения),
чтобы не настраивать отдельный веб-сервер.
"""
