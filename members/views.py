from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello new project")


def register_user(request):
    return HttpResponse("This is the register page")
