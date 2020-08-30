from django.contrib import admin

from .models import userProfile, UserPost

admin.site.register(userProfile)
admin.site.register(UserPost)

# Register your models here.
