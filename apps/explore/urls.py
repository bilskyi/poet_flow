from django.urls import path
from .views import *

urlpatterns = [
    path('poets/', classic_poets, name='explore'),
    path('users/', user_poets, name='user_poets'),
    path('<slug:slug>/', poet_detail, name='poet_detail'),
]