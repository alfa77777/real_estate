from django.urls import path

from houses.views import HousesListView, HouseDetailView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='homepage'),
    path("houses/", HousesListView.as_view(), name='houses_list'),
    path("house/<int:pk>/", HouseDetailView.as_view(), name='house_detail'),
]
