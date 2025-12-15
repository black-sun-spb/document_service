from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Document
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class DocumentModelTests(TestCase):

    def test_document_str(self):
        user = User.objects.create_user(email="model@test.com", password="12345")

        file = SimpleUploadedFile(
            "test.pdf", b"test content", content_type="application/pdf"
        )

        document = Document.objects.create(user=user, file=file)

        self.assertIn("Документ", str(document))
        self.assertIn(str(document.id), str(document))
