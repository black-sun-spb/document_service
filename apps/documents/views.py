from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import DocumentSerializer
from .tasks import notify_admin_new_document
from drf_spectacular.utils import extend_schema


@extend_schema(
    request={
        "multipart/form-data": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "format": "binary",
                    "description": "Файл документа для загрузки",
                }
            },
        }
    },
    responses={201: DocumentSerializer},
    description="Эндпоинт для загрузки документов пользователями.",
)
class DocumentUploadView(generics.CreateAPIView):
    """
    Создает новый документ в системе.

    - Требуется аутентификация пользователя.
    - При успешной загрузке документа отправляется уведомление администратору через Celery.
    - Ожидает multipart/form-data с ключом `file`.

    Атрибуты:
        serializer_class (DocumentSerializer): Сериализатор документа.
        permission_classes (list): Класс прав доступа (только аутентифицированные).
        parser_classes (tuple): Разбор multipart/form-data.
    """

    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        """
        Сохраняет документ с текущим пользователем и инициирует уведомление администратора.

        Args:
            serializer (DocumentSerializer): Сериализатор с данными запроса.
        """
        document = serializer.save(user=self.request.user)
        notify_admin_new_document.delay(document.id)
