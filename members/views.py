from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *


@login_required(login_url='login-user/')
def index(request):
    user = request.user
    return render(request, 'html/index.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login-user')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
                print(error)
                return render(request, 'html/register.html', {"form": form})
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-page')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'html/login.html', {})

    return render(request, 'html/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect('login-user')
