
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('register-user/', register_user, name='register-user'),
]