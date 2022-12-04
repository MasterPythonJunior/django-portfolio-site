from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def all_blog(request):
    blogs = Blog.objects.order_by('-date')  # Выдает по дате последние пять
    print(blogs)
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blogs = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blogs} )
