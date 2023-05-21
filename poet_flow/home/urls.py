from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='home'),
    path('home/', home, name='home'),
]