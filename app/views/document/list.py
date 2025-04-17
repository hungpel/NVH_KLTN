from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView

from app.models import Comment, Document, Subject


class DocumentListView(ListView):
    model = Document
    template_name = "pages/documents.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        subject = self.request.GET.get("subject")

        content_type = ContentType.objects.get_for_model(Document)
        for document in queryset:
            document.comment_count = Comment.objects.filter(
                content_type=content_type,
                object_id=document.pk,
            ).count()
        if subject:
            queryset = queryset.filter(subject=subject)
        return queryset
