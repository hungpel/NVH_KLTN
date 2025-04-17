from django.db import models

from .base import BaseModel


class Attachment(BaseModel):
    file = models.FileField(upload_to="attachments/")
