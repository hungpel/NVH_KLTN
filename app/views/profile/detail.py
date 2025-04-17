from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import DetailView

from app.models import Connect, Document, Like


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = "pages/profile.html"
    model = User

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        student = self.request.user.student
        content_type = ContentType.objects.get_for_model(Document).pk

        context["connects"] = Connect.objects.filter(
            owner=student,
        ).order_by("-created_at")
        context["documents"] = Document.objects.filter(
            owner=student,
        ).order_by("-created_at")
        likes = Like.objects.filter(
            owner=student,
            content_type=content_type,
        ).order_by("-created_at")
        context["likes"] = likes
        return context
