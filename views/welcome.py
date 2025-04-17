from django.views.generic import TemplateView


class WelcomePage(TemplateView):
    template_name = "pages/welcome_page.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "welcome_page"
        return self.render_to_response(context)
