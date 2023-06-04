from django.shortcuts import render
from home.models import Poet


def explore(request):
    poets = Poet.objects.all()
    return render(request, 'explore/explore.html', {'poets': poets})