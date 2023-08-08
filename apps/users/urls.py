from django.urls import path
from .views import *


urlpatterns = [
    # register, login and logout in poet_flow.urls
    path('add-poem/', add_poem, name='add_post'),
    path('settings/', settings, name='settings'),
    path('privacy/', privacy, name='privacy'),
    path('<slug:slug>/', profile, name='profile'),
    path('edit/<slug:user_slug>/<slug:poem_slug>/', edit_poem, name='edit_poem'),
    path('delete/<slug:user_slug>/<slug:poem_slug>/', delete_poem, name='delete_poem'),
]