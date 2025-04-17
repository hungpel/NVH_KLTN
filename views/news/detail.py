from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from djangocms_blog.models import Post


class DetailNewsPage(TemplateView):
    template_name = "pages/detail_news.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "detail_news"

        posts = Post.objects.order_by("-date_published").prefetch_related(
            "translations"
        )
        post = get_object_or_404(Post, pk=kwargs["post_id"])

        NUMBER_RELATED_NEWS = 4
        NUMBER_NEWS_TAGS = 3

        news_tags = post.tags.all()[:NUMBER_NEWS_TAGS]
        related_news = posts.exclude(pk=kwargs["post_id"])[
            :NUMBER_RELATED_NEWS
        ]

        context["post"] = post
        context["news_tags"] = news_tags
        context["related_news"] = related_news
        return self.render_to_response(context)
