from django.shortcuts import render
from .models import User
from .forms import UpdateUserForm


def profile(request, slug):
    user = User.objects.get(slug=slug)
    return render(request, 'users/profile.html', {'user': user})


def settings(request):
    form = UpdateUserForm()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})
