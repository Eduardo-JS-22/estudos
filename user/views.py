from django.shortcuts import render
from user.forms import LoginForm, RegisterForm

def login(request):
    form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout(request):
    return render(request, 'user/logout.html')

def register(request):
    form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})