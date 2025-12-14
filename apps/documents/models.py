from django.conf import settings
from django.db import models

class Document(models.Model):
    STATUS_NEW = 'NEW'
    STATUS_APPROVED = 'APPROVED'
    STATUS_REJECTED = 'REJECTED'

    STATUS_CHOICES = [
        (STATUS_NEW, 'Новый'),
        (STATUS_APPROVED, 'Подтвержден'),
        (STATUS_REJECTED, 'Отклонен'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name='Пользователь'
    )
    file = models.FileField(
        upload_to='documents/',
        verbose_name='Файл документа'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f'Документ #{self.id} ({self.status})'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
