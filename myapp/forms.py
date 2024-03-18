from django import forms
from .models import *


class CreateCarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            "model_name",
            "colour",
            "brand",
            "condition",

        ]

class CreateOwnerForm(forms.ModelForm):

    class Meta:
        model = Owner
        fields = ["name", "owned_from", "owned_to"]

class CreateColourForm(forms.ModelForm):

    class Meta:
        model = Colour
        fields = [
            "name",
            "paint_code"
        ]

class CreateBrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = [
            "name"
        ]
