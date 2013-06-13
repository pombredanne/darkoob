from django import forms
from django.utils.translation import ugettext as _

class NewReviewForm(forms.Form):
    text = forms.CharField(
        label=_('Text'),
        widget=forms.Textarea(attrs={
            'placeholder': _('Write Your Review about this book.'),
            'rows': 3,
            'class': 'span12',
            'style': 'resize: none;',
        })
    )
    title = forms.CharField(
        label=_('Book'),
        widget=forms.TextInput(attrs={
            'placeholder': _('Title of Review'),
            'autocomplete': 'off',
            'class': 'span10',
        })
    )    
