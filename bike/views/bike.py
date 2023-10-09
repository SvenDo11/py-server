from django.views import generic
from django.urls import reverse_lazy
from ..models import Bike

bike_fields = ["name", "manufacturer", "initial_odometer"]


class ListView(generic.ListView):
    template_name = 'bike/bike_list.html'
    context_object_name = 'bike_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context

    def get_queryset(self):
        return Bike.objects.all()


class DetailView(generic.DetailView):
    model = Bike
    template_name = 'bike/bike_detail.html'
    fields = bike_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        return context


class CreateView(generic.CreateView):
    model = Bike
    template_name = 'bike/t_create.html'
    fields = bike_fields
    success_url = reverse_lazy("bike:bikeList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        context['title'] = "Add Bike"
        context['header'] = "Add a new Bike"
        return context


class DeleteView(generic.DeleteView):
    model = Bike
    template_name_suffix = "_delete"
    success_url = reverse_lazy("bike:bikeList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        context['title'] = "Delete Bike"
        context['header'] = "Delete the Bike?"
        return context


class UpdateView(generic.UpdateView):
    model = Bike
    template_name = "bike/t_update.html"
    fields = bike_fields

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navigationbar_active'] = "bikes"
        context['title'] = "Edit Bike"
        context['header'] = "Edit the Bike:"
        return context
