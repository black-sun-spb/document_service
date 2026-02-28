from django.conf import settings
from django.db import models


class Document(models.Model):
    """
    Модель документа, загружаемого пользователем.

    Атрибуты:
        STATUS_NEW (str): Статус "Новый".
        STATUS_APPROVED (str): Статус "Подтвержден".
        STATUS_REJECTED (str): Статус "Отклонен".
        STATUS_CHOICES (list): Варианты выбора статуса.
        user (ForeignKey): Ссылка на пользователя, который загрузил документ.
        file (FileField): Файл документа.
        status (CharField): Текущий статус документа.
        created_at (DateTimeField): Дата и время создания документа.
    """

    STATUS_NEW = "NEW"
    STATUS_APPROVED = "APPROVED"
    STATUS_REJECTED = "REJECTED"

    STATUS_CHOICES = [
        (STATUS_NEW, "Новый"),
        (STATUS_APPROVED, "Подтвержден"),
        (STATUS_REJECTED, "Отклонен"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Пользователь",
    )
    file = models.FileField(upload_to="documents/", verbose_name="Файл документа")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Флаг: отправлено ли уведомление администратору
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        """
        Строковое представление документа.

        Returns:
            str: 'Документ #<id> (<status>)'.
        """
        return f"Документ #{self.id} ({self.status})"

    class Meta:
        """
        Метаданные модели.

        Атрибуты:
            verbose_name (str): Человекочитаемое имя модели в единственном числе.
            verbose_name_plural (str): Человекочитаемое имя модели во множественном числе.
        """

        verbose_name = "Документ"
        verbose_name_plural = "Документы"
