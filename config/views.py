from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from core.models import Post

def index(request):
    # faqat tasdiqlangan postlar
    approved_posts = Post.objects.filter(is_approved=True)

    # Eng yangi postlar
    latest_posts = approved_posts.order_by("-created_at")[:5]

    # Eng ko‘p ko‘rilgan postlar (umumiy)
    most_viewed = approved_posts.order_by("-views")[:5]

    # Haftaning eng ommabop postlari (7 kun ichida)
    week_ago = timezone.now() - timedelta(days=7)
    popular_week = approved_posts.filter(created_at__gte=week_ago).order_by("-views")[:5]

    # Oyning eng ommabop postlari (30 kun ichida)
    month_ago = timezone.now() - timedelta(days=30)
    popular_month = approved_posts.filter(created_at__gte=month_ago).order_by("-views")[:5]

    # Tavsiya qilingan postlar
    recommended_posts = approved_posts.filter(is_recommended=True)[:5]

    context = {
        "latest_posts": latest_posts,
        "most_viewed": most_viewed,
        "popular_week": popular_week,
        "popular_month": popular_month,
        "recommended_posts": recommended_posts,
    }
    return render(request, "home/index.html", context)
