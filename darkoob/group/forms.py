from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm

class GroupForm(forms.Form):
    name = forms.CharField(max_length=255)
    members = forms.CharField(widget=forms.HiddenInput())


