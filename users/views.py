from django.shortcuts import render, redirect
from .forms import LoginForm, RegForm
from django.contrib.auth import login as login_func, logout as logout_func

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
            # login = form.cleaned_data['login']
            # password = form.cleaned_data['password_1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # user = User.objects.create_user(username=login, password=password, first_name=first_name, last_name=last_name)

            return redirect('/')

    context = {'form': form}
    return render(request, 'users/reg_form.html', context)