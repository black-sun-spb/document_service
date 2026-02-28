from django.urls import path
from .views import DocumentUploadView

app_name = "documents"

urlpatterns = [
    # URL для загрузки документа через API
    path("upload/", DocumentUploadView.as_view(), name="document-upload"),
]
