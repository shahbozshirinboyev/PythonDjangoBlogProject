from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "profile_image", "password1", "password2")
