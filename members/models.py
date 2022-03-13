from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', default='media/default.jpeg')
    caption = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    project_pic = models.ImageField(upload_to='media', default='media/default.jpeg')
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=150, null=False, blank=False)
    live_link = models.URLField(null=True, blank=True)
    comments = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
