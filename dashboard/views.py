from django.views.generic import TemplateView

from dashboard.models import CarouselItem
from dashboard.models import CircleItem
from dashboard.models import FeatureItem

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
