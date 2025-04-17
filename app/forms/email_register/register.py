from typing import Any

from django import forms

from app.models import EmailRegister
from libs import BaseFormMixin


class EmailRegisterForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = EmailRegister
        fields = [
            "email",
        ]

    def save(self, commit: bool = ...) -> Any:
        instance = self.instance
        instance.save()
