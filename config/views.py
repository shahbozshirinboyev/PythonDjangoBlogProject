from django.shortcuts import render
from core.models import Post

def index(request):
    posts = Post.objects.filter(is_approved=True).order_by('-created_at')
    return render(request, 'home/index.html', {'posts': posts})
