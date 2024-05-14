from django.urls import path
from .views import (
    simcard_view,
    search_view,
    add_simcard_view,
    edit_simcard_view,
    delete_simcard_view,
)

urlpatterns = [
    path("", simcard_view, name="simcard-list"),
    path("search/results/", search_view, name="search-results"),
    path("add_simcard/", add_simcard_view, name="add-simcard"),
    path("<uuid:pk>/edit", edit_simcard_view, name="edit-simcard"),
    path("<uuid:pk>/delete", delete_simcard_view, name="delete-simcard"),
]