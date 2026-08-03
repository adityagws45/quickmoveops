from django import forms
from .models import Relocation


class RelocationForm(forms.ModelForm):

    class Meta:
        model = Relocation

        fields = [
            "customer_name",
            "phone",
            "email",
            "current_city",
            "destination_city",
            "move_date",
            "household_size",
            "property_type",
            "assigned_ops",
            "status",
        ]

        widgets = {
            "move_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
