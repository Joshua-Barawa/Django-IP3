from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['username', "first_name", "email", 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_pic', "name", "description", 'country', 'live_link']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['project_pic'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['live_link'].widget.attrs['class'] = 'form-control'


class RateForm(forms.ModelForm):
    class Meta:
        model = Prorating
        fields = ['design', "usability", "content"]

    def __init__(self, *args, **kwargs):
        super(RateForm, self).__init__(*args, **kwargs)
        self.fields['design'].widget.attrs['class'] = 'form-control'
        self.fields['usability'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['class'] = 'form-control'

