from django.views.generic import TemplateView


class UploadDocumentPage(TemplateView):
    template_name = "pages/upload_document.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["page_name"] = "upload_document"
        return self.render_to_response(context)
