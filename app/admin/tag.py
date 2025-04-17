from django.contrib import admin

from app.models import Tag


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
