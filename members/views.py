from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
from .forms import *


def index(request):
    return HttpResponse("Hello world")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('index-page')
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('index-page')
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {"form": form})
