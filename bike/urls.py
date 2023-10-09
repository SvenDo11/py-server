from django.urls import path

from .views import IndexView, bike, refueling, maintenance

app_name = 'bike'
urlpatterns = [
    path("", IndexView.as_view(), name="bikeIndex"),
    path("refueling/", refueling.ListView.as_view(), name="refuelingList"),
    path("refueling/<int:pk>/details/", refueling.DetailView.as_view(), name="refuelingDetail"),
    path("refueling/<int:pk>/delete/", refueling.DeleteView.as_view(), name='refuelingDelete'),
    path("refueling/<int:pk>/edit/", refueling.UpdateView.as_view(), name="refuelingUpdate"),
    path("refueling/addRefueling/", refueling.CreateView.as_view(), name="refuelingCreate"),
    path("bikes", bike.ListView.as_view(), name="bikeList"),
    path("bikes/<int:pk>/details/", bike.DetailView.as_view(), name="bikeDetail"),
    path("bikes/<int:pk>/delete/", bike.DeleteView.as_view(), name='bikeDelete'),
    path("bikes/<int:pk>/edit/", bike.UpdateView.as_view(), name="bikeUpdate"),
    path("bikes/addBike", bike.CreateView.as_view(), name="bikeCreate"),
    path("maintenance", maintenance.ListView.as_view(), name="maintenanceList"),
    path("maintenance/<int:pk>/details/", maintenance.DetailView.as_view(), name="maintenanceDetail"),
    path("maintenance/<int:pk>/delete/", maintenance.DeleteView.as_view(), name='maintenanceDelete'),
    path("maintenance/<int:pk>/edit/", maintenance.UpdateView.as_view(), name="maintenanceUpdate"),
    path("maintenance/addBike", maintenance.CreateView.as_view(), name="maintenanceCreate"),
]
