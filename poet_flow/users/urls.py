from django.urls import path
from .views import *


urlpatterns = [
    # register, login and logout in poet_flow.urls
    path('add-post/', add_post, name='add_post'),
    path('settings/', settings, name='settings'),
    path('<slug:slug>/', profile, name='profile'),
]