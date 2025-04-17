from django.contrib.auth.models import User
from django.db import models

from .base import BaseModel


class Student(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student"
    )
    avatar = models.FileField(upload_to="avatar/", blank=True, null=True)
    skills = models.ManyToManyField(
        "Skill",
        related_name="student_skills",
        blank=True,
    )
    hobbies = models.ManyToManyField(
        "Hobby",
        related_name="student_hobbies",
        blank=True,
    )
    school = models.CharField(default="", max_length=255, blank=True)
    code = models.CharField(default="", max_length=255, blank=True)
    classroom = models.CharField(default="", max_length=255, blank=True)
    fb_link = models.URLField(default="", blank=True, max_length=255)
    github_link = models.URLField(default="", blank=True, max_length=255)
    instagram_link = models.URLField(default="", blank=True, max_length=255)
    phone = models.CharField(default="", blank=True, max_length=255)
    address = models.CharField(default="", blank=True, max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
