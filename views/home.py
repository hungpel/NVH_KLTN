from django.views.generic import TemplateView
from djangocms_blog.models import Post

from app.models import Document, Slider


class HomePage(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        documents = Document.objects.filter().order_by("created_at")[:4]

        posts = Post.objects.order_by("-date_published")
        NUMBER_OUTSTANDING_NEWS = 6
        featured_news_list = posts[:NUMBER_OUTSTANDING_NEWS]

        context = self.get_context_data(**kwargs)

        context["documents"] = documents
        context["featured_news_list"] = featured_news_list

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"] = Slider.objects.all()
        return context
