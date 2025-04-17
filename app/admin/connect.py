from django.contrib import admin

from app.models import Connect


class ConnectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Connect, ConnectAdmin)
