from django.db import models

from .base import BaseModel


class Article(BaseModel):
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="post_students",
    )
    forum = models.ForeignKey(
        "Forum",
        on_delete=models.CASCADE,
        related_name="post_forums",
    )
    attachments = models.ManyToManyField(
        "Attachment",
        related_name="post_attachments",
        blank=True,
    )
    title = models.CharField(default="", max_length=255, blank=True)
    content = models.TextField(default="", max_length=5000, blank=True)
    tags = models.ManyToManyField(
        "Tag",
        related_name="post_tags",
        blank=True,
    )

    def __str__(self) -> str:
        return f"post {self.title} of {self.owner} in forum {self.forum}"
