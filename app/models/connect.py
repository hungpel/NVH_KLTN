from django.db import models

from .base import BaseModel


class Connect(BaseModel):
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="owner_connects",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(default="", max_length=2048, blank=True)
    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        related_name="subject_connects",
    )
    max_people = models.PositiveBigIntegerField(default=1)

    @property
    def count_connect(self):
        from app.models import ConnectTicket

        return ConnectTicket.objects.filter(connect=self).count()

    def __str__(self):
        return f"{self.name}"
