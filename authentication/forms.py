from django import forms
from django.forms import TextInput, EmailInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)