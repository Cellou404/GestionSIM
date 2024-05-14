from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(MobileDeviceType)
class MobileDeviceTypeAdmin(admin.ModelAdmin):
    list_display = ("code_name", "device_name")
    list_display_links = ("code_name",)
    list_filter = ["device_name"]
    search_fields = ["code_name"]
    list_per_page = 50


@admin.register(Asset)
class AssetsAdmin(ImportExportModelAdmin):
    list_display = (
        "lot",
        "imsi",
        "number",
        "device_type",
        "imei",
        "registration_number",
        "asset_description",
        "site",
        "plateforme",
    )
    list_display_links = ("imei", "device_type")
    search_fields = ("imei", "registration_number")
    list_filter = ("device_type", "site", "plateforme")
    list_per_page = 20
