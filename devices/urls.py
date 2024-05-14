from django.urls import path
from . import views

urlpatterns = [
    path("", views.devices, name="devices-list"),
    #path("devices_list", views.devices_list, name="devices-list"),
    path("search_device/results", views.search_device_view, name="device-results"),
    path("create/", views.device_create_view, name="add-device"),
    path("<uuid:pk>/edit/", views.device_edit_view, name="edit-device"),
    path("<uuid:pk>/delete/", views.device_delete_view, name="delete-device"),
    path("assets_count/", views.asset_count, name="assets-count"),
]

