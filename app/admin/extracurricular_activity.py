from django.contrib import admin

from app.models import ExtracurricularActivity


class ExtracurricularActivityAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExtracurricularActivity, ExtracurricularActivityAdmin)
