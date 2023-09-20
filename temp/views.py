from django.shortcuts import render
from django.views import generic

from typing import Any, Dict

from . import utils

# Create your views here.
class IndexView(generic.base.TemplateView):
    template_name = 'temp/home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        humidity, temperature = utils.get_humidity_temperature()
        context['room_temperature'] = temperature
        context['room_humidity'] = humidity
        return context

