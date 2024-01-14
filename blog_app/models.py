from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(default="", max_length=150, blank=False)
    article = models.TextField(default="",  max_length=450, blank=False)
    author = models.CharField(default="",  max_length=50, blank=False)
    description = models.CharField(default="",  max_length=1000, blank=False)
    image = models.ImageField(upload_to='post_image/', blank= True, null=True)
    secondary_image = models.URLField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    title = models.CharField(default="", max_length=100, blank=False)
    comment_body = models.TextField(default="", max_length=1000, blank=False)
    author = models.ForeignKey(User, on_delete=models.Case, null=True)
    to_post  = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Reel(models.Model):
    title = models.CharField(default="", max_length=20, blank=False)
    content_creator = models.CharField(default="", max_length=20, blank=False)
    description = models.CharField(default="", max_length=30, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title