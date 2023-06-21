from django.shortcuts import render
from home.models import Poet
from users.models import User


def classic_poets(request):
    poets = Poet.objects.all()
    selected_poets = 'classic'

    context = {
        'poets': poets,
        'selected_poets': selected_poets,
    }

    return render(request, 'explore/classic_poets.html', context=context)


def user_poets(request):
    poets = User.objects.all()
    selected_poets = 'user'

    context = {
        'poets': poets,
        'selected_poets': selected_poets,
    }

    return render(request, 'explore/user_poets.html', context=context)


def poet_detail(request, slug):
    
    try:
        poet = User.objects.get(slug=slug)
        
    except User.DoesNotExist:
        poet = Poet.objects.get(slug=slug)

    return render(request, 'explore/poet_detail.html', {'poet': poet})