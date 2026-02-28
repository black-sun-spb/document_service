from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Document.

    Используется для преобразования объекта Document в JSON и обратно.

    Поля:
        id (int): Идентификатор документа (только для чтения).
        file (File): Файл документа.
        status (str): Статус документа (только для чтения).
        created_at (datetime): Дата и время создания документа (только для чтения).
    """

    class Meta:
        model = Document
        fields = ("id", "file", "status", "created_at")
        read_only_fields = ("id", "status", "created_at")
