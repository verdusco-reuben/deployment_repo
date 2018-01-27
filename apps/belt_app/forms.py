from django import forms
from models import User


class LoginForm(forms.Form):
	email = forms.EmailField(label='Email')
	password = forms.CharField(label='Password', max_length=50,min_length=3)

