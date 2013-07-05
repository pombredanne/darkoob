from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm

class GroupForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': _('Group Name'),
            'class': 'input-medium ',
            'required': '',
        })
    )
    members = forms.CharField(required=False, widget=forms.HiddenInput())


class NewScheduleForm(forms.Form):
    book = forms.CharField(required=True, widget=forms.HiddenInput())


