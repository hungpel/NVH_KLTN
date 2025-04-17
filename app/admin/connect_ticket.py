from django.contrib import admin

from app.models import ConnectTicket


class ConnectTicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(ConnectTicket, ConnectTicketAdmin)
