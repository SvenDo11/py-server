from django.forms import DateTimeInput
from django.views import generic
from django.urls import reverse_lazy
from django_filters.views import FilterView
import django_filters as dj_filters

from ..models import Fuel
from ..plots import fuel_economy, fuel_price, fuel_odometer

refueling_fields = ["bike", "fuel_date", "quantity", "cost_per_litre", "total_cost", "km_trip", "km_total"]


class DateTimeWidget(DateTimeInput):
    input_type = "datetime-local"


class RefuelingFilter(dj_filters.FilterSet):
    fuel_date__gt = dj_filters.DateTimeFilter(field_name="fuel_date", lookup_expr='gt',
                                              label="From", widget=DateTimeWidget)
    fuel_date__lt = dj_filters.DateTimeFilter(field_name="fuel_date", lookup_expr='lt',
                                              label="Till", widget=DateTimeWidget)

    class Meta:
        model = Fuel
        fields = ['bike']


class ListView(FilterView):
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
            context['plot_1'] = fuel_economy(context['object_list'])
            context['plot_2'] = fuel_price(context['object_list'])
            context['plot_3'] = fuel_odometer(context['object_list'])
        return context


class DetailView(generic.DetailView):
    model = Fuel
    template_name = "bike/refueling_detail.html"
    fields = refueling_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        return context

    def get_queryset(self):
        return Fuel.objects.all()


class CreateView(generic.CreateView):
    model = Fuel
    template_name = 'bike/t_create.html'
    fields = refueling_fields
    success_url = reverse_lazy("bike:refuelingList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        context['title'] = "Add Refueling"
        context['header'] = "Add a new Refueling"
        return context


class DeleteView(generic.DeleteView):
    model = Fuel
    template_name = "bike/t_delete.html"
    success_url = reverse_lazy("bike:refuelingList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        context['title'] = "Delete Refueling"
        context['header'] = "Delete the Refueling?"
        return context


class UpdateView(generic.UpdateView):
    model = Fuel
    template_name = "bike/t_update.html"
    fields = refueling_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "refueling"
        context['title'] = "Edit Refueling"
        context['header'] = "Edit Refueling:"
        return context
