from django.db import models
from django.contrib.auth.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', default='media/default.png')
    caption = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    project_pic = models.ImageField(upload_to='media', default='media/default.png')
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=150, null=False, blank=False)
    country = models.CharField(max_length=100, default="No specified", null=False, blank=False)
    posted_at = models.DateField(default=datetime.date.today)
    live_link = models.URLField(null=True, blank=True)
    comments = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
