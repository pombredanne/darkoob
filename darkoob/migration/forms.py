from django import forms
from django.utils.translation import ugettext as _

class StartNewMigrationForm(forms.Form):

    book = forms.CharField(
        label=_('Book'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Book Name'),
            'autocomplete': 'off',
            'data-provide': 'typeahead',
            'class': 'span6 typeahead',
            'id': 'title-look',
        })
    )

    starter_message = forms.CharField(
        label=_('Your Message '),
        widget=forms.Textarea(attrs={
            'placeholder': _('Your Message'),
            'rows': 7,
            'class': 'span8',
        })
    )