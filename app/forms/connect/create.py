from typing import Any

from django import forms

from app.models import Connect
from libs import BaseFormMixin


class ConnectCreateForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Connect
        fields = ["name", "description", "subject", "max_people"]

    def save(self, commit: bool = ...) -> Any:
        user = self.request.user
        instance = self.instance
        instance.owner = user.student
        instance.save()
