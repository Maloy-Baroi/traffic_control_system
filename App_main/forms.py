from django import forms
from App_main.models import CaseModel


class CaseModelForm(forms.ModelForm):
    occurrence_happened_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = CaseModel
        exclude = ['accused', 'registered_by', ]
