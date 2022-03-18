
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('register-user/', register_user, name='register-user'),
    path('login-user/', login_user, name='login-user'),
    path('logout/', logout_user, name='logout-user'),
    path('submit-project/', submit_project, name='submit-project'),
    path('view-project/<int:id>', view_project, name='view-project'),
    path('profile/', my_profile, name='profile'),
    path('project-list/', project_list, name='project-list'),
    path('user-list/', user_list, name='user-list'),
]