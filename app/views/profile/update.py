from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from app.forms import ProfileUpdateForm
from app.models import Student


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "pages/update_profile.html"
    model = Student
    form_class = ProfileUpdateForm

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user.student

    def get_success_url(self) -> str:
        success_url = reverse_lazy("profile")
        return success_url
