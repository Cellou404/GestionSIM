from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Site, Plateforme
from simcard.models import SimCard


class MobileDeviceType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code_name = models.CharField(_("code name"), max_length=20, help_text=_("e.g: fmb140"))
    device_name = models.CharField(_("device name"), max_length=50, help_text=_("e.g: Teltonika FMB140"))
    description = models.TextField(_("description"),  max_length=500, help_text=_("500 characters allowed"), blank=True, null=True,)

    class Meta:
        verbose_name = _("Mobile Device Type")
        verbose_name_plural = _("Mobile Device Types")
    def __str__(self):
        return f"{self.device_name}"


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    lot = models.CharField(max_length=10, db_default="Lot ?")  # Lot number of the sim card
    imsi = models.CharField(max_length=16, null=True, blank=True)  # IMSI number of the sim card
    number = models.CharField(max_length=16, null=True, blank=True)  # phone number of the sim card
    device_type = models.CharField(max_length=150, null=True, blank=True)
    imei = models.CharField(max_length=16)
    registration_number = models.CharField(_("registration number"), max_length=50)
    asset_description = models.CharField(_("asset description"), max_length=50)
    site = models.CharField(max_length=200, null=True, blank=True)
    plateforme = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Asset")
        verbose_name_plural = _("Assets")
        ordering = ['imei']
