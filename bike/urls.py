from django.urls import path

from . import views

app_name = 'bike'
urlpatterns = [
    path("", views.IndexView.as_view(), name="bikeIndex"),
    path("refueling", views.FuelingView.as_view(), name="refuelingList"),
    path("allBikes", views.BikeListView.as_view(), name="bikeList"),
    path("<int:pk>/delete/", views.BikeDeleteView.as_view(), name='bikeDelete'),
]
