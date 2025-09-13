from django.views.generic import TemplateView, ListView, DetailView
from core.models import Post, Comment

class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5

class CommentListView(ListView):
    model = Comment
    template_name = "blog/comments.html"
    context_object_name = "comments"
    ordering = ["-created_at"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj
