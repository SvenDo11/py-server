from django.shortcuts import render
from django.views import generic
from .models import Bike, Fuel


class FuelingView(generic.ListView):
    template_name = 'bike/fueling.html'
    context_object_name = 'fueling_list'

    def get_queryset(self):
        return Fuel.objects.order_by('-fuel_date')


class AddBikeView(generic.CreateView):
    model = Bike
    fields = ["name"]
