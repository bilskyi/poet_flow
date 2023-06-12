from django.urls import path
from .views import *


urlpatterns = [
    path('settings/', settings, name='settings'),
    path('<slug:slug>/', profile, name='profile'),
]