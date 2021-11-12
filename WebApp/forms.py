from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.db import models
from django import forms


class signupform(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}


class loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'username', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password', 'placeholder': 'Password'}))
