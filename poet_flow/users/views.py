from django.shortcuts import render
from .models import User
from .forms import UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied



def profile(request, slug):
    user = User.objects.get(slug=slug)
    return render(request, 'users/profile.html', {'user': user})

@login_required
def settings(request):
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user )
        if form.is_valid():
            form.save()
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})
