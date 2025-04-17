from django.views.generic import TemplateView


class UpdateProfilePage(TemplateView):
    template_name = "pages/update_profile.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "update_profile"
        return self.render_to_response(context)
