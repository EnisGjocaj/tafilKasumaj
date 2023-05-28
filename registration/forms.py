from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, help_text='')

	class Meta:
		model = User
		fields = ("username" ,"email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'fields'
		self.fields['email'].widget.attrs['class'] = 'fields'
		self.fields['password1'].widget.attrs['class'] = 'fields'
		self.fields['password2'].widget.attrs['class'] = 'fields'

		self.fields['username'].widget.attrs['id'] = 'username-field'
		self.fields['email'].widget.attrs['id'] = 'email-field'
		self.fields['password1'].widget.attrs['id'] = 'pas1-field'
		self.fields['password2'].widget.attrs['id'] = 'pas2-field'

		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

		self.fields['password1'].help_text = ''
		self.fields['password2'].help_text = ''
		self.fields['username'].help_text = ''
		self.fields['email'].help_text = ''



