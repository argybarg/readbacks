from django import forms

from .models import Unit, Reading


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading