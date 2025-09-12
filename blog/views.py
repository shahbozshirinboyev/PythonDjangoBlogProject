from django.shortcuts import render

def posts_view(request):
    return render(request, "blog/posts.html")

def comments_view(request):
    return render(request, "blog/comments.html")
