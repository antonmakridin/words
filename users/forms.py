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

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)
    
    def get_user(self):
        return self.user

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        self.user = authenticate(self.request, username=login, password=password)
        if not self.user:
            raise forms.ValidationError('Неверный логин или пароль')
        
        return self.cleaned_data
    

    
class RegForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
        label='Придумайте логин:',
        )
    password_1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
        label='Пароль:',
        )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
        label='Повторите пароль:',
        )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Имя'}),
        label='Имя:',
        required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}),
        label='Фамилия:',
        required=False)
    
    def clean_login(self):
        login = self.cleaned_data['login']
        if User.objects.filter(username=login).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует')
        return login

    def clean(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data