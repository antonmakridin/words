from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm
from django.contrib.auth import login as login_func, logout as logout_func, authenticate
from .models import *

def login(request):
    
    form = LoginForm(request)

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            login_func(request, form.get_user())
            return redirect('main')

    context = {'form': form}

    return render(request, 'users/login.html', context)

def logout_view(request):
    logout_func(request)
    return redirect('main')


def reg_form(request):
    form = RegForm()

    if request.method == 'POST':
        form = RegForm(request.POST)

        if form.is_valid():
            # создание пользователя и профиля

            username = form.cleaned_data['login']
            password = form.cleaned_data['password_1']

            # создание пользователя
            user = User(username=username)
            user.set_password(password)
            user.save()

            # создание профиля пользователя
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            profile = Profile(user=user,first_name=first_name, last_name=last_name)
            profile.save()

            # авторизуем пользователя
            user = authenticate(request, username=user.username, password=password)
            login_func(request, user)

            return redirect('/')

    context = {'form': form}
    return render(request, 'users/reg_form.html', context)