from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class Site(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(_("Name of site"), max_length=50)
    address = models.CharField(_("Address of site"), max_length=100)
    latitude = models.FloatField(_("latitude"), blank=True, null=True)
    longitude = models.FloatField(_("longitue"), blank=True, null=True)
    altitude = models.PositiveSmallIntegerField(_("longitue"), help_text=_('Altitude in meters'), blank=True, null=True,)

    def __str__(self):
        return f"{self.name} ({self.address})"
    
class Plateforme(models.Model):
    """A platform is a place where users can connect to their devices"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(_('Platform Name'), max_length=30)
    description = models.TextField(_('Description of Platform'), max_length=500, help_text=_('500 characters allowed.'), blank=True, null=True,)

    def __str__(self) -> str:
        return self.name

