from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home.as_view(), name='home'),
    ]
