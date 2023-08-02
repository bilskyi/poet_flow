from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib.auth import login, authenticate, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from home.models import Poet, UserPoem


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
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
            poem.author = request.user
            poem.save()
            form.save_m2m()  # Save the many-to-many relationships after saving the poem instance
            request.user.poems.add(poem)
            return redirect('home')
    else:
        form = AddPost()

    return render(request, 'home/add_poem.html', {'form': form})


def profile(request, slug):
    try:
        poet = User.objects.get(slug=slug)
        return render(request, 'users/base_user.html', {'poet': poet})
    except User.DoesNotExist:
        poet = Poet.objects.get(slug=slug)
        return render(request, 'explore/poet_detail.html', {'poet': poet})


@login_required
def settings(request):

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES,
                              instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})


@login_required
def edit_poem(request, user_slug, poem_slug):
    poem = get_object_or_404(UserPoem, slug=poem_slug)
    if request.method == 'POST':
        form = AddPost(request.POST, instance=poem)
        if form.is_valid():
            if not form.changed_data:
                pass
            else:
                updated_poem = form.save()
                return redirect('edit_poem', user_slug=user_slug, poem_slug=updated_poem.slug)
    else:
        form = AddPost(instance=poem)
    return render(request, 'users/edit_poem.html', {'form': form, 'poem': poem})