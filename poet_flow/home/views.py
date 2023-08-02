from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *

from django.contrib.auth.forms import AuthenticationForm
from users.models import User

from .models import ClassicPoem, UserPoem

def welcome(request):
    bar = SearchForm()
    return render(request, 'home/welcome.html', {'bar': bar})


def home(request):
    poems = ClassicPoem.objects.all()
    return render(request, 'home/home.html', {'poems': poems})


def view_detail(request, poet_slug, poem_slug):
    try:
        poem = UserPoem.objects.get(slug=poem_slug)
    except:
        poem = ClassicPoem.objects.get(slug=poem_slug)
    return render(request, 'home/view_detail.html', {'poem': poem})


def search(request):
    form = SearchForm()
    return form