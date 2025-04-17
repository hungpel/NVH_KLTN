from django.views.generic import TemplateView


class AddRequestPage(TemplateView):
    template_name = "pages/add_request.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "add_request"
        return self.render_to_response(context)
