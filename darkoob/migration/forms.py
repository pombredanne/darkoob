from django import forms
from django.utils.translation import ugettext as _

class StartNewMigrationForm(forms.Form):
    # TODO: this field should be autho complete
    book_title = forms.CharField(
        label = _('Book Title'),
        widget = forms.TextInput(attrs={
            'placeholder': _('Book Title'),
        })
    )
    # book_id = forms.CharField(
    #     widget = forms.HiddenInput(attrs={
    #     })
    # )
    starter_message = forms.CharField(
        label = _('Your Message'),
        widget = forms.TextInput(attrs={
            'placeholder': _('Your Message'),
        })
    )

