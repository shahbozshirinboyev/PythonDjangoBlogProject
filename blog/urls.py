from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path('posts/pending/', views.pending_posts, name='pending_posts'),
    path('posts/<int:pk>/approve/', views.approve_post, name='approve_post'),
]