from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import validate_email
from django.contrib.auth.forms import AuthenticationForm

SEX_CHOICES = (
    ('Male', _('Male')),
    ('Female', _('Female')),
)
MONTH_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
)

class AuthenticationFormPlaceholder(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'class': 'input-medium',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'class': 'input-medium'
        })
    )

class EditProfileForm(forms.Form):
    month = forms.ChoiceField(choices = MONTH_CHOICES)

    day = forms.CharField(
        label = _('Day'),
        min_length = 1,
        max_length = 2,
        widget = forms.TextInput(attrs={
            'placeholder':_('Day'),
            'id': 'day',
        })
    )

    year = forms.CharField(
        label = _('Year'),
        min_length = 4,
        max_length = 4,
        widget = forms.TextInput(attrs={
            'placeholder':_('Year'),
        })
    )

    sex = forms.ChoiceField(
        choices = SEX_CHOICES,
    )

class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        label = _('Password'),
        min_length = 3,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Password'),
        })
    )

    new_password = forms.CharField(
        label = _('New password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('New password'),
        })
    )

    confirm_new_password = forms.CharField( # Why?!
        label = _('Re-type new password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Re-type new password'),
        })
    )

    def clean_confirm_new_password(self):
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if confirm_new_password != self.cleaned_data['new_password']:
            raise forms.ValidationError(_('New password and Re-type does not match'))
        return confirm_new_password

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label = _('First Name'), 
        min_length = 2, 
        max_length = 30,
        widget = forms.TextInput(attrs={
            'placeholder':_('First Name'),
        })
    )

    last_name = forms.CharField(
        label = _('Last Name'),
        min_length = 2,
        max_length = 30,
        widget = forms.TextInput(attrs={
            'placeholder':_('Last Name'),			
        })
    )
    email = forms.EmailField(
        label = _('E-Mail'),
        min_length = 5,
        widget = forms.TextInput(attrs={
            'placeholder': _('Your email address'),
        })
    )
    password = forms.CharField(
        label = _('Password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Password'),
        })
    )
    confirm_password = forms.CharField(
        label = _('Re-type password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Re-type password'),
        })
    )

    sex = forms.ChoiceField(choices=SEX_CHOICES)
    month = forms.ChoiceField(choices=MONTH_CHOICES)

    day = forms.CharField(
        label = _('Day'),
        min_length = 1,
        max_length = 2,
        widget = forms.TextInput(attrs={
            'placeholder':_('Day'),
        })
    )

    year = forms.CharField(
        label = _('Year'),
        min_length = 4,
        max_length = 4,
        widget = forms.TextInput(attrs={
            'placeholder':_('Year'),
        })
    )

    def clean_day(self):
        day = int(self.cleaned_data['day'])
        if (day > 31 or day < 1):
            raise forms.ValidationError(_('Invalid date'))
        return day

    def clean_month(self):
        month = int(self.cleaned_data['month'])
        if (month > 12 or month < 1):
            raise forms.ValidationError(_('Invalid date'))
        return month

    def clean_year(self):
        year = int(self.cleaned_data['year'])
        if (year > 2012 or year < 1900):
            raise forms.ValidationError(_('Invalid date'))
        return year

    def clean_email(self):
        email = self.cleaned_data['email']
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(email=email) 
        except User.DoesNotExist:
            return email
        else:
            # E-mail is a uniqe field 
            raise forms.ValidationError(_('You are member! Did you forget your password?'))

    def clean_password(self):
        password = self.cleaned_data['password']
        # Check strog password
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        if confirm_password != self.cleaned_data['password']:
            raise forms.ValidationError(_('Password and Re-type does not match'))
        return confirm_password

