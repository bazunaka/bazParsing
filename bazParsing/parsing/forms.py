from django import forms
from .models import Development


class FindForm(forms.Form):
    development = forms.ModelChoiceField(queryset=Development.objects.all())
