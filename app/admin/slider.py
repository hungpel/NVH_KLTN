from django.contrib import admin

from app.models import Slider


class SliderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Slider, SliderAdmin)
