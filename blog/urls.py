from django.urls import path
from .views import PostListView, CommentListView, PostDetailView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("comments/", CommentListView.as_view(), name="comments"),
]