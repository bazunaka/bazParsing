from django import forms
from .models import Development


class FindForm(forms.Form):
    development = forms.ModelChoiceField(queryset=Development.objects.all(), to_field_name='name',
                                         widget=forms.Select(attrs={'class': 'form-control'}),
                                         label='Застройщик')

