from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views.decorators.csrf import csrf_protect

from .forms import CustomUserCreationForm

@csrf_protect
def logout_confirm(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "accounts/logout.html")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Ro‘yxatdan keyin avtomatik login
            return redirect("index")  # Bosh sahifaga yuborish
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})