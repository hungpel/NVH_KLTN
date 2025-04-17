from typing import Any

from django import forms

from app.models import Document
from libs import BaseFormMixin


class DocumentCreateForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            "name",
            "subject",
            "description",
            "file",
        ]

    def save(self, commit: bool = ...) -> Any:
        user = self.request.user
        instance = self.instance
        instance.owner = user.student
        instance.save()
