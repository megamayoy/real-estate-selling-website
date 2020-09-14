from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render


def login(request):
    return render(request, "accounts/login.html")


def register(request):
    if request.method == 'POST':
        messages.success(request, "registration completed")
        return redirect('index')
    return render(request, "accounts/register.html")


def logout(request):
    return redirect("index")


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
