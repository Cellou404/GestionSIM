from django import forms
from .models import SimCard


class SimCardForm(forms.ModelForm):
    class Meta:
        model = SimCard
        fields = ["lot" , "imsi", "number", "status", "in_stock", "comment"]