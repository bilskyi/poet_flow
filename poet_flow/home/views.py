from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserAuthenticationForm, AddPost
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Poem

def welcome(request):
    return render(request, 'home/welcome.html')


def home(request):
    poems = Poem.objects.all()
    return render(request, 'home/home.html', {'poems': poems})


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
            poem.user_author = request.user
            poem.save()
            form.save_m2m()  # Save the many-to-many relationships after saving the poem instance
            return redirect('home')
    else:
        form = AddPost()
    
    return render(request, 'home/add_poem.html', {'form': form})


def view_detail(request, poem_slug):
    poem = Poem.objects.get(slug=poem_slug)

    return render(request, 'home/view_detail.html', {'poem':poem})