from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .base import BaseModel


class Like(BaseModel):
    owner = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="likes"
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="content_likes"
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return f"{self.owner} like {self.content_object}"
