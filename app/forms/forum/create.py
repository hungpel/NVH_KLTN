from typing import Any

from django import forms

from app.models import Forum
from libs import BaseFormMixin


class ForumCreateForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Forum
        fields = [
            "name",
            "description",
            "category",
        ]

    def save(self, commit: bool = ...) -> Any:
        user = self.request.user
        instance = self.instance
        instance.owner = user.student
        instance.save()
