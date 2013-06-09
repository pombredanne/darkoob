from django import forms
from django.utils.translation import ugettext as _

class StartNewMigrationForm(forms.Form):
    # TODO: this field should be autho complete

    starter_message = forms.CharField(
        label=_('Your Message '),
        widget=forms.Textarea(attrs={
            'placeholder': _('Your Message'),
            'rows': 7,
            'class': 'span8',
        })
    )