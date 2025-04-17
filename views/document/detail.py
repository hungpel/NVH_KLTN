from django.views.generic import TemplateView


class DetailDocumentPage(TemplateView):
    template_name = "pages/detail_document.html"


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["page_name"] = "detail_document"
        return self.render_to_response(context)

