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
            'id': 'id_username_auth',
            'placeholder': _('Username'),
            'class': 'input-medium',
            'required': '',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'id_password_auth',
            'placeholder': _('Password'),
            'class': 'input-medium required',
            'required': '',
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

    mobile = forms.CharField(
        label = _('Mobile'),
        min_length = 7,
        max_length = 20,
        widget = forms.TextInput(attrs={
            'placeholder':_('Mobile'),
        })
    )

    website = forms.CharField(
        label = _('Website'),
        min_length = 4,
        max_length = 100,
        widget = forms.TextInput(attrs={
            'placeholder':_('Website'),
        })
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
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'class': 'span12 required',
            'required': '',
        }))

    first_name = forms.CharField(
        label = _('First Name'), 
        min_length = 2, 
        max_length = 30,
        widget = forms.TextInput(attrs={
            'placeholder':_('First Name'),
            'class': 'span6 required',
            'required': '',
        })
    )

    last_name = forms.CharField(
        label = _('Last Name'),
        min_length = 2,
        max_length = 30,
        widget = forms.TextInput(attrs={
            'placeholder':_('Last Name'),
            'class': 'span6 required',
            'required': '',
        })
    )
    email = forms.EmailField(
        label = _('E-Mail'),
        min_length = 5,
        widget = forms.TextInput(attrs={
            'placeholder': _('Your email address'),
            'type': 'email',
            'class': 'span12 required',
            'required': '',
        })
    )
    password = forms.CharField(
        label = _('Password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Password'),
            'class': 'span6 required',
            'required': '',
        })
    )
    confirm_password = forms.CharField(
        label = _('Re-type password'),
        min_length = 6,
        max_length = 30,
        widget = forms.PasswordInput(attrs={
            'placeholder':_('Re-type password'),
            'class': 'span6',
            'required': '',
        })
    )

    sex = forms.ChoiceField(choices=SEX_CHOICES)
    month = forms.ChoiceField(choices=MONTH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'span4',
        })
    )

    day = forms.CharField(
        label = _('Day'),
        min_length = 1,
        max_length = 2,
        widget = forms.TextInput(attrs={
            'placeholder':_('Day'),
            'class': 'span4',
            'required': '',
        })
    )

    year = forms.CharField(
        label = _('Year'),
        min_length = 4,
        max_length = 4,
        widget = forms.TextInput(attrs={
            'placeholder':_('Year'),
            'class': 'span4',
            'required': '',
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

class NewPostForm(forms.Form):
    text = forms.CharField(
        label=_('Text'),
        widget=forms.Textarea(attrs={
            'placeholder': _('Say it!'),
            'rows': 3,
            'class': 'span12',
            'style': 'resize: none;',
        })
    )

