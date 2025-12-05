from django import forms
from .models import *
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
        label='Логин:'
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
        label='Пароль:'
        )
    
    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        # user = authenticate(username=login, password=password)