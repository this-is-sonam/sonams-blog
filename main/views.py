from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
    blogs = Blog.objects.all().order_by('-id')   # newest first
    return render(request, "main/home.html", {
        "blogs": blogs
    })


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, "main/blog_detail.html", {
        "blog": blog
    })
