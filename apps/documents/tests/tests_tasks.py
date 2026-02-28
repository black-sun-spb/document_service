from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.documents.models import Document
from apps.documents.tasks import notify_user_document_status

User = get_user_model()


class DocumentTasksTests(TestCase):

    def test_notify_user_document_status_sends_email(self):
        user = User.objects.create_user(email="task@test.com", password="12345")

        file = SimpleUploadedFile("test.pdf", b"test", content_type="application/pdf")

        document = Document.objects.create(
            user=user, file=file, status=Document.STATUS_APPROVED
        )

        notify_user_document_status(document.id)

        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("Ваш документ", mail.outbox[0].subject)
