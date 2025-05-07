from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView
from app.models import Comment, Document, Subject
from app.ai.search_engine import search_documents  # giữ lại import này


class DocumentListView(ListView):
    model = Document
    template_name = "pages/documents.html"  # đảm bảo file đúng
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        context["query"] = self.request.GET.get("q", "")
        context["selected_subject"] = self.request.GET.get("subject", "")
        return context

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        subject = self.request.GET.get("subject", "")

        if query:
            # Dùng AI để tìm tài liệu theo query
            results = search_documents(query)
            if subject:
                results = [doc for doc in results if doc.subject and str(doc.subject.id) == subject]
            return results
        else:
            queryset = Document.objects.all()
            if subject:
                queryset = queryset.filter(subject__id=subject)
            return queryset

