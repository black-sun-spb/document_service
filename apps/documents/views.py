from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import DocumentSerializer
from .tasks import notify_admin_new_document
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter

@extend_schema(
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'file': {
                    'type': 'string',
                    'format': 'binary',
                }
            }
        }
    }
)

class DocumentUploadView(generics.CreateAPIView):
    """
    API для загрузки документов зарегистрированными пользователями.
    После загрузки отправляется уведомление администратору (Celery).
    """
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        document = serializer.save(user=self.request.user)
        notify_admin_new_document.delay(document.id)
