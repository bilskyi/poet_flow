from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm, AddPost
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


def welcome(request):
    return render(request, 'home/welcome.html')


def home(request):
    return render(request, 'home/home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})


def login_user(request):
    form = UserAuthenticationForm()
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                            password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect('home')
    form = UserAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

@login_required()
def logout_user(request):
    logout(request)
    return redirect('welcome')


@login_required(login_url='/login/')
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)  # Bind the form data to the form instance
        if form.is_valid():
            poem = form.save(commit=False)
            poem.user_author = request.user  # Set the user_author field to the current user
            poem.save()
            return redirect('home')  # Redirect to the desired page after successful submission
    else:
        form = AddPost()
    
    return render(request, 'home/add_poem.html', {'form': form})