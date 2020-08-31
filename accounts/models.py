from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User

from likes.models import Like


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.user.name

class UserPost(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date_post = models.DateTimeField(null=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models
                             .CASCADE)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
