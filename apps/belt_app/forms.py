from django import forms
from django.forms import ModelForm
from models import User

class UserForm(ModelForm):
	password_confirm = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['name','alias','email','password']

class LoginForm(forms.Form):
	email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password', max_length=50,min_length=2)
