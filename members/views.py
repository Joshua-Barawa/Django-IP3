from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


@login_required(login_url='login-user/')
def index(request):
    projects = Project.objects.all()
    return render(request, 'html/index.html', {'projects': projects})


@login_required(login_url='login-user/')
def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            prorating = Prorating()
            prorating.pro_name = project
            prorating.save()
            messages.success(request, "Project was submitted successful")
            return redirect('index-page')
    else:
        form = ProjectForm()
        return render(request, 'html/project-form.html', {'form': form})

    return render(request, 'html/project-form.html', {'form': form})


@login_required(login_url='login-user/')
def view_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == "POST":
        form = RateForm(request.POST)

        if form.is_valid():
            pro = Prorating.objects.get(pro_name=project)

            if int(form['design'].value()) > 10 or int(form['design'].value()) < 0:
                messages.success(request, "Design cannot be less than 0 or greater than 10 ")
            elif int(form['usability'].value()) > 10 or int(form['usability'].value()) < 0:
                messages.success(request, "Usability cannot be less than 0 or greater than 10 ")
            elif int(form['content'].value()) > 10 or int(form['content'].value()) < 0:
                messages.success(request, "Content cannot be less than 0 or greater than 10 ")
            else:
                pro.count = pro.count + 1
                pro.design = (int(pro.design) + int(form['design'].value())) / pro.count
                pro.usability = (int(pro.usability) + int(form['usability'].value())) / pro.count
                pro.content = (int(pro.content) + int(form['content'].value())) / pro.count
                pro.save()
                messages.success(request, "Project was rated/reviewed successful")

    else:
        form = RateForm()
    return render(request, 'html/project-page.html', {"project": project, 'form': form})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('index-page')
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
