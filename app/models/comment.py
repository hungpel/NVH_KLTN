from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .base import BaseModel


class Comment(BaseModel):
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="comment_students",
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    text = models.CharField(default="", max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.owner} comment in {self.content_object}"
