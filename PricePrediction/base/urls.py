
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('laptop/', laptop, name='laptop'),
    path('result/', laptop, name='result'),
]
