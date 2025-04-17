from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    image = models.FileField(upload_to="sliderIMG/")

    def __str__(self) -> str:
        return self.name
