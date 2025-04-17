from django.views.generic import TemplateView


class SendRequestPage(TemplateView):
    template_name = "pages/send_request.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "send_request"
        return self.render_to_response(context)
