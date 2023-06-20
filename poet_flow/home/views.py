from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from users.models import User

from .models import ClassicPoem

def welcome(request):
    return render(request, 'home/welcome.html')


def home(request):
    poems = ClassicPoem.objects.all()
    return render(request, 'home/home.html', {'poems': poems})



def view_detail(request, poet_slug, poem_slug):
    poem = ClassicPoem.objects.get(slug=poem_slug)
    return render(request, 'home/view_detail.html', {'poem':poem})
