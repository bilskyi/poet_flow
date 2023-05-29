from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('explore/', home, name='explore'),
    path('home/', home, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-post/', add_post, name='add_post'),
    path('poem/<slug:poem_slug>/', view_detail, name='view_detail'),
]