from django.views.generic import ListView

from app.models import Document


class DocumentListView(ListView):
    model = Document
    template_name = "pages/documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


