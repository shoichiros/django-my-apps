from django import forms
from accounts.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="")
    password = forms.CharField(label="", max_length=255, widget=forms.PasswordInput)

    username.widget.attrs.update({'placeholder': 'Username'})
    password.widget.attrs.update({'placeholder': 'Password'})
