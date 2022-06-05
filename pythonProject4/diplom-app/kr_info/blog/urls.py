from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogPage.as_view(), name='blogs'),
    ]



