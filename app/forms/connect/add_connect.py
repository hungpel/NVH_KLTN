from typing import Any

from django import forms

from app.models import ConnectTicket
from libs import BaseFormMixin


class AddConnectForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = ConnectTicket
        fields = ["message", "connect"]

    def save(self, commit: bool = ...) -> Any:
        user = self.request.user
        instance = self.instance
        instance.student = user.student
        instance.save()
