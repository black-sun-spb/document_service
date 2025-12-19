from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from apps.documents.models import Document

User = get_user_model()


class DocumentUploadTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com", password="test12345"
        )
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.url = reverse("documents:document-upload")

    def test_user_can_upload_document(self):
        file = SimpleUploadedFile(
            "test.pdf", b"%PDF-1.4 test content", content_type="application/pdf"
        )

        response = self.client.post(self.url, {"file": file}, format="multipart")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Document.objects.count(), 1)

        document = Document.objects.first()
        self.assertEqual(document.user, self.user)
        self.assertEqual(document.status, Document.STATUS_NEW)

    def test_anonymous_user_cannot_upload_document(self):
        self.client.credentials()  # убираем токен

        file = SimpleUploadedFile(
            "test.pdf", b"%PDF-1.4 test content", content_type="application/pdf"
        )

        response = self.client.post(self.url, {"file": file}, format="multipart")

        self.assertEqual(response.status_code, 403)
