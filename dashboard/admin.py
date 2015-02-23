from django.contrib import admin

from dashboard.models import Page
from dashboard.models import CarouselItem
from dashboard.models import CircleItem
from dashboard.models import FeatureItem


class PageAdmin(admin.ModelAdmin):
    pass


class CarouselItemAdmin(admin.ModelAdmin):
    pass


class CircleItemAdmin(admin.ModelAdmin):
    pass


class FeatureItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
admin.site.register(CarouselItem, CarouselItemAdmin)
admin.site.register(CircleItem, CircleItemAdmin)
admin.site.register(FeatureItem, FeatureItemAdmin)
