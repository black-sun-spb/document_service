from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.documents.admin import DocumentAdmin
from apps.documents.models import Document

User = get_user_model()


class DocumentAdminTests(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.admin = DocumentAdmin(Document, self.site)

    def test_change_status(self):
        user = User.objects.create_user(email="admin@test.com", password="12345")

        file = SimpleUploadedFile("test.pdf", b"test", content_type="application/pdf")

        document = Document.objects.create(user=user, file=file)

        self.admin._change_status_and_notify(
            Document.objects.filter(id=document.id), Document.STATUS_APPROVED
        )

        document.refresh_from_db()
        self.assertEqual(document.status, Document.STATUS_APPROVED)
