from django.views.generic import TemplateView


class CoupleFriendPage(TemplateView):
    template_name = "pages/couple_friends.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "couple_friends"
        return self.render_to_response(context)
