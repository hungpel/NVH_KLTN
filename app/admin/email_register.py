from django.contrib import admin

from app.models import EmailRegister


class EmailRegisterAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailRegister, EmailRegisterAdmin)
