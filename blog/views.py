from django.shortcuts import render
from blog.models import Blog

def blog_list_view(request):
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

