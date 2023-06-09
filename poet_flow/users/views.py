from django.shortcuts import render
from .models import User

def profile(request, slug):
    user = User.objects.get(slug=slug)
    return render(request, 'users/profile.html', {'user': user})