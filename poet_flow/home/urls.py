from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]