from django.contrib import admin

from app.models import Forum


class ForumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Forum, ForumAdmin)
