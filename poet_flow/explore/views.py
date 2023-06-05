from django.shortcuts import render
from home.models import Poet


def explore(request):
    poets = Poet.objects.all()
    return render(request, 'explore/explore.html', {'poets': poets})


def poet_detail(request, slug):
    poet = Poet.objects.get(slug=slug)
    return render(request, 'explore/poet_detail.html', {'poet': poet})