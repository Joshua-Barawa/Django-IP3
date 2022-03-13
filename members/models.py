from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(blank=True, null=True)
    caption = models.TextField(max_length=200)
