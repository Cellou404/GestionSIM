from django.contrib import admin
from core.models import Site, Plateforme


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "latitude",
        "longitude",
        "altitude",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 20


@admin.register(Plateforme)
class PlateformeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 20
