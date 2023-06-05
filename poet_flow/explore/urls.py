from django.urls import path
from .views import *

urlpatterns = [
    path('', explore, name='explore'),
    path('<slug:slug>/', poet_detail, name='poet-detail'),
]