from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Email'
    )

    password = forms.CharField(
        max_length=60,
        required=True,
        label='Password',
        widget=forms.PasswordInput
    )

