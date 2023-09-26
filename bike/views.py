from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .models import Bike, Fuel
from .plots import get_test_plot, fuel_economy
import django_filters as dj_filters

bike_fields = ["name", "manufacturer", "initial_odometer"]
refueling_fields = ["bike", "fuel_date", "quantity", "cost_per_litre", "total_cost", "km_trip", "km_total"]


class IndexView(generic.TemplateView):
    template_name = "bike/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "home"
        return context


class RefuelingFilter(dj_filters.FilterSet):
    fuel_date__gt = dj_filters.DateTimeFilter(field_name="fuel_date", lookup_expr='gt', label="From")
    fuel_date__lt = dj_filters.DateTimeFilter(field_name="fuel_date", lookup_expr='lt', label="Till")

    class Meta:
        model = Fuel
        fields = ['bike']


class RefuelingListView(FilterView):
    model = Fuel
    template_name = 'bike/refueling_list.html'
    context_object_name = 'fueling_list'
    filterset_class = RefuelingFilter
    showClear = False

    def get(self, request, *args, **kwargs):
        self.showClear = any(field in request.GET for field in
                             set(self.filterset_class.get_fields()))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        if self.showClear:
            context['display_clear'] = "true"
        if len(context['object_list']) > 0:
            context['plot'] = fuel_economy(context['object_list'])
        return context


class RefuelingDetailView(generic.DetailView):
    model = Fuel
    template_name = "bike/refueling_detail.html"
    fields = refueling_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context

    def get_queryset(self):
        return Fuel.objects.all()


class RefuelingCreateView(generic.CreateView):
    model = Fuel
    template_name = 'bike/bike_create.html'
    fields = refueling_fields
    success_url = reverse_lazy("bike:refuelingList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context


class RefuelingDeleteView(generic.DeleteView):
    model = Fuel
    template_name = "bike/refueling_delete.html"
    success_url = reverse_lazy("bike:refuelingList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context


class RefuelingUpdateView(generic.UpdateView):
    model = Fuel
    template_name = "bike/refueling_update.html"
    fields = refueling_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context


class BikeListView(generic.ListView):
    template_name = 'bike/bike_list.html'
    context_object_name = 'bike_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context

    def get_queryset(self):
        return Bike.objects.all()


class BikeDetailView(generic.DetailView):
    model = Bike
    template_name = 'bike/bike_detail.html'
    fields = bike_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context


class BikeCreateView(generic.CreateView):
    model = Bike
    template_name = 'bike/bike_create.html'
    fields = bike_fields
    success_url = reverse_lazy("bike:bikeList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context


class BikeDeleteView(generic.DeleteView):
    model = Bike
    template_name_suffix = "_delete"
    success_url = reverse_lazy("bike:bikeList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context


class BikeUpdateView(generic.UpdateView):
    model = Bike
    template_name = "bike/bike_update.html"
    fields = bike_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context
