from django import forms
from core.models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Izoh qoldiring..."
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "category", "tags"]
