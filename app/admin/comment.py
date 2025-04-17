from django.contrib import admin

from app.models import Comment


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
