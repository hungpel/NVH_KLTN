from django.views.generic import ListView

from app.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "pages/news.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
