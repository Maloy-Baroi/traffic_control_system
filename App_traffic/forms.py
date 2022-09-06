from django import forms
from App_traffic.models import *


class TrafficModelForm(forms.ModelForm):
    class Meta:
        model = TrafficOfficerModel
        exclude = ['user', ]


