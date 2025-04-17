from django.db import models

from .base import BaseModel


class Forum(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(default="", max_length=2048, blank=True)
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="forums",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="category_forums",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
