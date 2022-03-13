
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('register-user/', register_user, name='register-user'),
    path('login-user/', login_user, name='login-user'),
    path('logout/', logout_user, name='logout-user'),
    path('submit-project/', submit_project, name='submit-project'),
]