from django.urls import path
from .views import *
from users import views

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('search/', search_view, name='search'),
    path('poem/<slug:poet_slug>/<slug:poem_slug>/', view_detail, name='view_detail'),
]