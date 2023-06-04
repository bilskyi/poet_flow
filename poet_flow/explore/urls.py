from django.urls import path
from .views import *

urlpatterns = [
    path('', explore, name='explore'),
]