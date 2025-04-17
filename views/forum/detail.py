from django.views.generic import TemplateView


class DetailForumPage(TemplateView):
    template_name = "pages/detail_forum.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        context["page_name"] = "detail_forum"
        return self.render_to_response(context)
