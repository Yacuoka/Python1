from django.shortcuts import render
from django.views.generic import ListView

from .models import *

menu = [
    {'title': 'Войти', 'url_name': 'index'},
]


class BlogPage(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        # context['cat_selected'] = 0
        context['menu'] = menu
        return context

    # def get_queryset(self):
    #     return blog.objects.filter(is_published=True).select_related('cat')

