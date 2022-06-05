from django.shortcuts import render

from .models import *

menu = [
    {'title': 'Войти', 'url_name': 'index'},
]


def home(request):
    return render(request, 'main_info/index.html')