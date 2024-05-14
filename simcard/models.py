from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

class SimCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    SIM_STATUS = (
        ("ok", "OK"),  # The SIM is working properly
        ("broken", "BROKEN"), # SIM not working
        ("lost", "LOST"),  # The SIM has been lost and cannot be found
        ("stolen", "STOLEN"),  # The SIM has been stolen
    )
    lot = models.CharField(max_length=10, db_default="Lot ?")  # Lot number of the sim card
    imsi = models.PositiveIntegerField(unique=True)  # IMSI number of the sim card
    number = models.PositiveIntegerField(unique=True)  # phone number of the sim card
    status = models.CharField(
        max_length=20, 
        choices=SIM_STATUS,
        default=SIM_STATUS[0][0],
    )  # Status code for the sim card
    in_stock = models.BooleanField(_("In stock"), default=True)  # Is this item available or not?
    comment = models.TextField(max_length=500,  blank=True, null=True)  # Additional comments about the sim card
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return str(self.number)
    

