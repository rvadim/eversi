from django.views.generic import TemplateView
from django.views.generic import DetailView

from dashboard.models import CarouselItem
from dashboard.models import CircleItem
from dashboard.models import FeatureItem
from dashboard.models import Page

import logging

log = logging.getLogger(__name__)


class Base(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        return {
            'carousel': CarouselItem.objects.all(),
            'circle': CircleItem.objects.all(),
            'feature': FeatureItem.objects.all(),
        }


class PageView(DetailView):
    model = Page
    template_name = 'page_detail.html'
