from django.urls import path

from . import views

app_name = 'bike'
urlpatterns = [
    path("", views.IndexView.as_view(), name="bikeIndex"),
    path("refueling/", views.RefuelingListView.as_view(), name="refuelingList"),
    path("refueling/<int:pk>/details/", views.RefuelingDetailView.as_view(), name="refuelingDetail"),
    path("refueling/<int:pk>/delete/", views.RefuelingDeleteView.as_view(), name='refuelingDelete'),
    path("refueling/<int:pk>/edit/", views.RefuelingUpdateView.as_view(), name="refuelingUpdate"),
    path("refueling/addRefueling", views.RefuelingCreateView.as_view(), name="refuelingCreate"),
    path("bikes", views.BikeListView.as_view(), name="bikeList"),
    path("bikes/<int:pk>/details/", views.BikeDetailView.as_view(), name="bikeDetail"),
    path("bikes/<int:pk>/delete/", views.BikeDeleteView.as_view(), name='bikeDelete'),
    path("bikes/<int:pk>/edit/", views.BikeUpdateView.as_view(), name="bikeUpdate"),
    path("bikes/addBike", views.BikeCreateView.as_view(), name="bikeCreate"),
]
