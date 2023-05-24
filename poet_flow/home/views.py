from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def welcome(request):
    return render(request, 'home/welcome.html')


def home(request):
    return render(request, 'home/home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserRegister()
    return render(request, 'home/register.html', {'form': form})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                            password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('welcome')