from django.db import models
from django.contrib.auth.models import User
import datetime
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    profile_pic = CloudinaryField()
    caption = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    project_pic = CloudinaryField()
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=150, null=False, blank=False)
    country = models.CharField(max_length=100, default="No specified", null=False, blank=False)
    posted_at = models.DateField(default=datetime.date.today)
    live_link = models.URLField(null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Prorating(models.Model):
    pro_name = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pro_name.name)


class Comment(models.Model):
    pro_name = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return str(self.commenter.username)

