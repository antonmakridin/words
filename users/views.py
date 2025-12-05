from django.shortcuts import render, redirect
from .forms import LoginForm

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        context = {'form': form}    
        return render(request, 'users/login.html', context)