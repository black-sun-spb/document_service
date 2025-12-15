from django.contrib import admin
from .models import Document
from .tasks import notify_user_document_status


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Административная панель для модели Document.

    Атрибуты:
        list_display (tuple): поля, отображаемые в списке документов.
        list_filter (tuple): фильтры в боковой панели админки.
        actions (list): доступные действия для выбора нескольких документов.
    """

    list_display = ("id", "user", "status", "created_at")
    list_filter = ("status", "created_at")
    actions = ["approve_documents", "reject_documents"]

    def save_model(self, request, obj, form, change):
        """
        Вызывается при сохранении объекта через админку.

        Если объект обновляется (change=True) и его статус изменился,
        отправляется уведомление пользователю через Celery задачу.

        Args:
            request (HttpRequest): объект запроса.
            obj (Document): сохраняемый объект документа.
            form (ModelForm): форма объекта документа.
            change (bool): True если объект обновляется, False если создаётся.
        """
        if change:
            old_obj = Document.objects.get(pk=obj.pk)
            super().save_model(request, obj, form, change)

            if old_obj.status != obj.status:
                print(
                    f"[DEBUG] Status changed for Document #{obj.id}, sending email to {obj.user.email}"
                )
                notify_user_document_status.delay(obj.id)
        else:
            super().save_model(request, obj, form, change)

    def _change_status_and_notify(self, queryset, new_status):
        """
        Вспомогательный метод для массового изменения статуса документов
        и отправки уведомлений пользователям.

        Args:
            queryset (QuerySet): выбранные объекты Document.
            new_status (str): новый статус, который будет установлен.
        """
        queryset.update(status=new_status)
        for doc in queryset:
            print(
                f"[DEBUG] Changing status of Document #{doc.id} to {new_status}, sending email to {doc.user.email}"
            )
            notify_user_document_status.delay(doc.id)

    @admin.action(description="Подтвердить документы")
    def approve_documents(self, request, queryset):
        """
        Действие администратора для подтверждения выбранных документов.

        Args:
            request (HttpRequest): объект запроса.
            queryset (QuerySet): выбранные объекты Document.
        """
        self._change_status_and_notify(queryset, Document.STATUS_APPROVED)

    @admin.action(description="Отклонить документы")
    def reject_documents(self, request, queryset):
        """
        Действие администратора для отклонения выбранных документов.

        Args:
            request (HttpRequest): объект запроса.
            queryset (QuerySet): выбранные объекты Document.
        """
        self._change_status_and_notify(queryset, Document.STATUS_REJECTED)
