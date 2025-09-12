from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.posts_view, name="posts"),
    path("comments/", views.comments_view, name="comments"),
]
