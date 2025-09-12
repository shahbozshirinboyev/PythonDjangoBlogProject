from django.contrib import admin
from .models import Category, Tag, Post, Comment, CustomUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "is_approved", "is_recommended", "created_at")
    list_filter = ("is_approved", "is_recommended", "category", "created_at")
    search_fields = ("title", "content")
    autocomplete_fields = ("category", "author", "tags")  


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("content",)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "date_joined")
    search_fields = ("username", "email")
