from django.db import models


class EmailRegister(models.Model):
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.email
