from typing import Any

from django import forms
from django.db import transaction

from app.models import Student


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Student
        fields = [
            "code",
            "address",
            "classroom",
            "phone",
            "avatar",
            "email",
        ]

    @transaction.atomic
    def save(self, commit=True) -> Any:
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]

        instance = self.instance
        user = instance.user

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if commit:
            user.save(update_fields=["first_name", "last_name", "email"])
        instance.save()
