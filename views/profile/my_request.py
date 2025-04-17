from django.views.generic import TemplateView


class MyRequestPage(TemplateView):
    template_name = "pages/my_request.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "my_request"
        return self.render_to_response(context)
