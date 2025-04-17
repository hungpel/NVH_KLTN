from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView

from app.models import Category, Comment, Forum, Like, Tag


class ForumListView(ListView):
    model = Forum
    template_name = "pages/forum.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category")
        content_type = ContentType.objects.get_for_model(Forum)
        for forum in queryset:
            forum.like_count = Like.objects.filter(
                content_type=content_type,
                object_id=forum.pk,
            ).count()
            forum.comment_count = Comment.objects.filter(
                content_type=content_type,
                object_id=forum.pk,
            ).count()
        if category:
            queryset = queryset.filter(category=category)
        return queryset
