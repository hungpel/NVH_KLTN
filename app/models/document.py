from django.db import models

from .base import BaseModel


class Document(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/", blank=True, null=True)
    description = models.TextField(default="", max_length=1000, blank=True)
    owner = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="documents"
    )
    subject = models.ForeignKey(
        "Subject",
        related_name="subject_documents",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"
