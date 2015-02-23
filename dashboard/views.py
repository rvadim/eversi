from django.views.generic import TemplateView

from dashboard.models import CarouselItem

import logging

log = logging.getLogger(__name__)


class Base(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        return {
            'carousel': CarouselItem.objects.all(),
        }
