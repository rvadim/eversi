from django.contrib import admin

from dashboard.models import Page
from dashboard.models import CarouselItem
from dashboard.models import CircleItem
from dashboard.models import FeatureItem
from django import forms

from ckeditor.widgets import CKEditorWidget


class PageAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page


class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm


class CarouselItemAdminForm(forms.ModelForm):
    cut = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CarouselItem


class CarouselItemAdmin(admin.ModelAdmin):
    form = CarouselItemAdminForm


class CircleItemAdminForm(forms.ModelForm):
    cut = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = CircleItem


class CircleItemAdmin(admin.ModelAdmin):
    form = CircleItemAdminForm


class FeatureItemAdminForm(forms.ModelForm):
    cut = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FeatureItem


class FeatureItemAdmin(admin.ModelAdmin):
    form = FeatureItemAdminForm


admin.site.register(Page, PageAdmin)
admin.site.register(CarouselItem, CarouselItemAdmin)
admin.site.register(CircleItem, CircleItemAdmin)
admin.site.register(FeatureItem, FeatureItemAdmin)
