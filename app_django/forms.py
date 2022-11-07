from django import forms
from .models import Town, Street


class AddressForm(forms.Form):
    # town = Town.objects.all()
        # filter(site_data__id=1)
    name = forms.ModelChoiceField(queryset=Town.objects.all(), label='Город')
    street = forms.ModelChoiceField(queryset=Street.objects.filter(town=Town.))
    # Student.objects.select_related('school').get(pk=1)
    # Town.street_set, label='Улица')