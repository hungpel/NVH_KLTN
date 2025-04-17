from django.views.generic import TemplateView


class ProfilePage(TemplateView):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "profile"
        return self.render_to_response(context)
