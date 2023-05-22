from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='home'),
    path('home/', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]