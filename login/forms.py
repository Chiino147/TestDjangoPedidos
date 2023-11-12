from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)