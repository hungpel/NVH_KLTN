from django.db import models


class Hobby(models.Model):
    name = models.CharField(default="", blank=True, max_length=255)

    def __str__(self) -> str:
        return self.name
