from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Bike, Fuel


class IndexView(generic.TemplateView):
    template_name = "bike/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "home"
        return context


class FuelingView(generic.ListView):
    template_name = 'bike/refueling_list.html'
    context_object_name = 'fueling_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context

    def get_queryset(self):
        return Fuel.objects.order_by('-fuel_date')


class BikeListView(generic.ListView):
    template_name = 'bike/bike_list.html'
    context_object_name = 'bike_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context

    def get_queryset(self):
        return Bike.objects.all()


class BikeCreateView(generic.CreateView):
    model = Bike
    fields = ["name"]
    success_url = reverse_lazy("bike:bikeList")


class BikeDeleteView(generic.DeleteView):
    model = Bike
    template_name_suffix = "_delete"
    success_url = reverse_lazy("bike:bikeList")
