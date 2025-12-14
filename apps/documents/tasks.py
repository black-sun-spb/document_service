from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Document

@shared_task
def notify_admin_new_document(document_id):
    document = Document.objects.get(id=document_id)
    send_mail(
        subject=f'Новый документ #{document.id}',
        message=f'Пользователь {document.user.username} загрузил документ #{document.id}.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],  # email админа
        fail_silently=False,
    )

@shared_task
def notify_user_document_status(document_id):
    document = Document.objects.get(id=document_id)
    send_mail(
        subject=f'Ваш документ #{document.id} теперь {document.status}',
        message=f'Ваш документ #{document.id} теперь {document.status}.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[document.user.email],
        fail_silently=False,
    )
