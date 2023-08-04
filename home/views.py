from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm
from users.models import User

from .models import ClassicPoem, UserPoem

def welcome(request):
    return render(request, 'home/welcome.html')


def home(request):
    poems = ClassicPoem.objects.all()
    return render(request, 'home/home.html', {'poems': poems})


def view_detail(request, poet_slug, poem_slug):
    try:
        poem = UserPoem.objects.get(slug=poem_slug)
    except:
        poem = ClassicPoem.objects.get(slug=poem_slug)
    return render(request, 'home/view_detail.html', {'poem': poem})


def search_view(request):
    query = request.GET.get('query')
    user_poems_query = Q(title__icontains=query)
    classic_poems_query = Q(title__icontains=query)
    combined_query = user_poems_query | classic_poems_query
    if query:
        results = list(UserPoem.objects.filter(combined_query)) + list(ClassicPoem.objects.filter(combined_query))
    else:
        results = []
    return render(request, 'home/search.html', {'results': results})