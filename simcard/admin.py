from django.contrib import admin
from .models import *
from .forms import SimCardForm


@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    form = SimCardForm
    list_display = (
        "lot",
        "imsi",
        "number",
        "status",
        "in_stock",
        "created_at",
        "updated_at",
    )
    list_display_links = ("lot", "imsi")
    list_filter = ("lot", "status", "in_stock")
    search_fields = ["lot", "imsi"]
    list_per_page = 25
