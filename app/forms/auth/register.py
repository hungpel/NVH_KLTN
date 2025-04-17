from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from app.models import Student


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    code = forms.CharField(required=True)
    classroom = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

    @transaction.atomic
    def save(self, commit: bool = ...) -> Any:
        super().save(commit)
        code = self.cleaned_data["code"]
        classroom = self.cleaned_data["classroom"]
        instance = self.instance

        Student.objects.create(
            user=instance,
            code=code,
            classroom=classroom,
            avatar="/static/img/default_user_icon.jpg",
        )
        return instance
