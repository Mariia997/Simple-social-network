from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import userProfileListCreateView, userProfileDetailListView, UserPostView, UsersAPI

urlpatterns = [
    path('all-profiles', userProfileListCreateView.as_view(), name='all-profiles'),
    path('profile/<int:pk>', userProfileDetailListView.as_view(), name='profile'),
    path('all_users', UsersAPI.as_view(), name='all_users' ),
    path('create_post', UserPostView.as_view(), name='create_post'),
]