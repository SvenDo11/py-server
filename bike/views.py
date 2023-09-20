from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Bike, Fuel


class IndexView(generic.TemplateView):
    template_name = "bike/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FuelingView(generic.ListView):
    template_name = 'bike/fueling.html'
    context_object_name = 'fueling_list'

    def get_queryset(self):
        return Fuel.objects.order_by('-fuel_date')


class AddBikeView(generic.CreateView):
    model = Bike
    fields = ["name"]
    success_url = "http://127.0.0.1:8000/bike"


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = 'bike/bike_detail.html'
