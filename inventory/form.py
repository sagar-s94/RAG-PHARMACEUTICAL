from django import forms
from .models import add_stock
from .models import out_stock


class addstock_form(forms.ModelForm):
    class Meta:
        model= add_stock
        fields="__all__"

class outstock_form(forms.ModelForm):
    class Meta:
        model=out_stock
        fields="__all__"


