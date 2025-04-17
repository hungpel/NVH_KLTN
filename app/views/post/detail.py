from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.models import Article
from libs import BaseViewMixin


class ArticleDetailView(LoginRequiredMixin, BaseViewMixin, DetailView):
    model = Article
    template_name = "pages/detail_news.html"
