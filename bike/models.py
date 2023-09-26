from unicodedata import decimal
from django.db import models
from django.urls import reverse_lazy


class Fuel(models.Model):
    bike = models.ForeignKey("Bike", models.CASCADE)
    fuel_date = models.DateTimeField('date fueled up')
    quantity = models.DecimalField('Amount fueled up', max_digits=5, decimal_places=2)
    cost_per_litre = models.DecimalField('Cost per litre', max_digits=5, decimal_places=3)
    total_cost = models.DecimalField('Total cost of fueling', max_digits=5, decimal_places=2)
    km_trip = models.IntegerField('Km since last fueling')
    km_total = models.IntegerField('Total Km of the bike')

    def __str__(self) -> str:
        return "Fueling on {}: {}€".format(self.fuel_date, self.total_cost)

    def litre_per_100km(self) -> decimal:
        return self.quantity / self.km_trip * 100

    def get_absolute_url(self):
        return reverse_lazy("bike:refuelingDetail", kwargs={"pk": self.id})


class Maintenance(models.Model):
    bike = models.ForeignKey("Bike", models.CASCADE)
    date = models.DateTimeField('Date of maintenance work')
    maintenance_type = models.IntegerField('Type of done maintenance work')
    cost = models.DecimalField('Total cost of maintenance', max_digits=3, decimal_places=2)

    def __str__(self) -> str:
        return "{} done on {}".format(self.maintenance_type, self.date)


class Bike(models.Model):
    ID = models.IntegerField("ID", primary_key=True)
    name = models.CharField('Name', max_length=30)
    manufacturer = models.CharField('Manufacturer', max_length=30)
    initial_odometer = models.IntegerField("Initial Odometer Reading", default = 0)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("bike:bikeDetail", kwargs={"pk": self.ID})
