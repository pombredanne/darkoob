from django import forms

SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
MONTH_CHOICES = (
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'),
	(6,'6'),
	(7,'7'),
	(8,'8'),
	(9,'9'),
	(10,'10'),
	(11,'11'),
	(12,'12'),
)
class RegisterForm(forms.Form):
	first_name = forms.CharField(
		label = "firstname", 
		min_length = 2, 
		max_length = 30,
		widget = forms.TextInput(attrs={
			'placeholder':'First Name',
		}))

	last_name = forms.CharField(
		label = "lastname",
		min_length = 2,
		max_length = 30,
		widget = forms.TextInput(attrs={
			'placeholder':'Last Name',			
		}))
	email = forms.EmailField(
		label = 'email',
		min_length = 5,
		widget = forms.TextInput(attrs={
			'placeholder': 'Your email address',
		}))
	password = forms.CharField(
		label = "Password",
		min_length = 8,
		max_length = 30,
		widget = forms.PasswordInput(attrs={
			'placeholder':'Password',
		}))
	confirm_password = forms.CharField(
		label = "rePassword",
		min_length = 8,
		max_length = 30,
		widget = forms.PasswordInput(attrs={
			'placeholder':'Re-type password',
		}))

	sex = forms.ChoiceField(choices=SEX_CHOICES)	
	
	month = forms.ChoiceField(choices=MONTH_CHOICES)
	
	day = forms.CharField(
		label = "Day",
		min_length = 1,
		max_length = 2,
		widget = forms.TextInput(attrs={
			'placeholder':"Day",
		}))
		
	year = forms.CharField(
		label = "Year",
		min_length = 4,
		max_length = 4,
		widget = forms.TextInput(attrs={
			'placeholder':"Year",
		}))
		
	
	def clean_day(self):	
 		day = int(self.cleaned_data['day'])
		if (day>31 or day<1):
			raise forms.ValidationError("Invalid date")
		return day
		
	def clean_month(self):
		month= int(self.cleaned_data['month'])
		if (month >12 or month<1):
			raise forms.ValidationError("Invalid date")
		
		return month

	def clean_year(self):
		year= int(self.cleaned_data['year'])
		if (year >2012 or year<1900):
			raise forms.ValidationError("Invalid date")
		return year
		




