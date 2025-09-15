from django.views.generic import TemplateView, ListView, DetailView
from core.models import Post
from .forms import CommentForm, PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(is_approved=True).order_by("-created_at")

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=["views"])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comments.all()
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """Comment form yuborilganda ishlaydi"""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


# faqat staff foydalanuvchilar kira oladi
@user_passes_test(lambda u: u.is_staff)
@login_required
def pending_posts(request):
    posts = Post.objects.filter(is_approved=False)
    return render(request, 'admin/pending_posts.html', {'posts': posts})

@user_passes_test(lambda u: u.is_staff)
@login_required
def approve_post(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=False)
    post.is_approved = True
    post.save()
    return redirect('pending_posts')

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # hozirgi foydalanuvchini muallif qilish
            post.save()
            form.save_m2m()  # teglarni saqlash
            return redirect("index")  # qo‘shilgandan keyin bosh sahifaga qaytarish
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})
