from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def logout_confirm(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")  
    return render(request, "accounts/logout.html")
