from django.forms import DateInput
from django.views import generic
from django.urls import reverse_lazy
from django_filters.views import FilterView
import django_filters as dj_filters

from ..models import Maintenance
from ..plots import fuel_economy, fuel_price, fuel_odometer

maintenance_fields = ["bike", "date", "maintenance_type", "cost"]


class DateWidget(DateInput):
    input_type = "date"


class MaintenanceFilter(dj_filters.FilterSet):
    date__gt = dj_filters.DateTimeFilter(field_name="date", lookup_expr='gt',
                                         label="From", widget=DateWidget)
    date__lt = dj_filters.DateTimeFilter(field_name="date", lookup_expr='lt',
                                         label="Till", widget=DateWidget)

    class Meta:
        model = Maintenance
        fields = ['bike']


class ListView(FilterView):
    model = Maintenance
    template_name = 'bike/maintenance_list.html'
    context_object_name = 'maintenance_list'
    filterset_class = MaintenanceFilter
    showClear = False

    def get(self, request, *args, **kwargs):
        self.showClear = any(field in request.GET for field in
                             set(self.filterset_class.get_fields()))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "maintenance"
        if self.showClear:
            context['display_clear'] = "true"
        return context


class DetailView(generic.DetailView):
    model = Maintenance
    template_name = "bike/maintenance_detail.html"
    fields = maintenance_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "maintenance"
        return context

    def get_queryset(self):
        return Maintenance.objects.all()


class CreateView(generic.CreateView):
    model = Maintenance
    template_name = 'bike/t_create.html'
    fields = maintenance_fields
    success_url = reverse_lazy("bike:maintenanceList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "maintenance"
        context['title'] = "Create Maintenance"
        context['header'] = "Create a new Maintenance Entry:"
        return context


class DeleteView(generic.DeleteView):
    model = Maintenance
    template_name = "bike/t_delete.html"
    success_url = reverse_lazy("bike:maintenanceList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "maintenance"
        context['title'] = "Delete Maintenance"
        context['header'] = "Delete the Maintenance Entry?"
        return context


class UpdateView(generic.UpdateView):
    model = Maintenance
    template_name = "bike/t_update.html"
    fields = maintenance_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "Maintenance"
        context['title'] = "Edit Maintenance"
        context['header'] = "Edit the Maintenance Entry:"
        return context
