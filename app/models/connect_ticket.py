from django.db import models

from .base import BaseModel


class ConnectTicket(BaseModel):
    connect = models.ForeignKey(
        "Connect",
        on_delete=models.CASCADE,
        related_name="connect_tickets",
    )
    message = models.TextField(default="", max_length=1000, blank=True)
    accepted = models.BooleanField(default=False)
    student = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="student_connect_tickets",
    )

    def __str__(self):
        return f"{self.message}"
