# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Grant',
        'title': 'Blog Post 1',
        'content': 'This is the content of blog post 1',
        'date_posted': 'July 8, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is the content of blog post 2',
        'date_posted': 'July 9, 2020'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 3',
        'content': 'This is the content of blog post 3',
        'date_posted': 'July 10, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
