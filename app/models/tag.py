from django.db import models


class Tag(models.Model):
    name = models.CharField(default="", max_length=255, blank=True)
    background_color = models.CharField(default="", max_length=255, blank=True)
    selected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
