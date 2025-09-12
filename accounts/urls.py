from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_confirm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path("logout/", logout_confirm, name="logout"),
]
