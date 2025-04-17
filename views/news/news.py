from django.core.paginator import Paginator
from django.views.generic import TemplateView
from djangocms_blog.models import Post


class NewsPage(TemplateView):
    # Nen dung list view
    template_name = "pages/news.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["page_name"] = "news"

        posts = Post.objects.order_by("-date_published").prefetch_related(
            "translations"
        )

        PAGE_SIZE = 8
        paginator = Paginator(posts, PAGE_SIZE)

        current_news_page_number = request.GET.get("page", 1)
        try:
            current_news_page_number = int(current_news_page_number)
        except ValueError:
            print("Error: 'page' is not an integer")
            current_news_page_number = 1

        news_paginator = paginator.get_page(current_news_page_number)

        current_page_index = []
        for index in range(PAGE_SIZE):
            current_page_index.append(
                (current_news_page_number - 1) * PAGE_SIZE + index + 1
            )

        context["posts"] = posts
        context["news_paginator"] = news_paginator
        context["current_page_index"] = current_page_index

        return self.render_to_response(context)
