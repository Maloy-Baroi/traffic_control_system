from django import forms
from App_driver.models import DriverModel


class DriverModelForm(forms.ModelForm):
    class Meta:
        model = DriverModel
        exclude = ['user', ]


