from django.views.generic import TemplateView


class AddForumPage(TemplateView):
    template_name = "pages/add_forum.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["page_name"] = "add_forum"
        return self.render_to_response(context)
