from django.db import models
from django.contrib.auth.models import User


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
    date_post = models.DateTimeField()
    user = models.ForeignKey(userProfile, related_name='posts', on_delete=models
                             .CASCADE)
    post_like = models.IntegerField(null=True)
    post_unlike = models.IntegerField(null=True)

    def __str__(self):
        return self.title
