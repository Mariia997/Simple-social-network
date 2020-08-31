from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import userProfile, UserPost
from .permissions import IsOwnerProfileOrReadOnly
from rest_framework.permissions import IsAdminUser
from .serializers import userProfileSerializer, UserPostSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class userProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = (
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)



class UsersAPI(ListCreateAPIView):

    permission_classes = (
        IsAdminUser,
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class userProfileDetailListView(RetrieveUpdateDestroyAPIView):
    queryset =  userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class UserPostView(APIView):
    def get(self, request):
        user_post = UserPost.objects.all()
        serializer = UserPostSerializer(user_post, many=True)
        return Response({'user_post': serializer.data})

    def post(self, request):
        user_post = request.data.get('user_post')
        serializer = UserPostSerializer(data=user_post)
        if serializer.is_valid(raise_exception=True):
            user_post_saved = serializer.save()
        return Response({'success': "Post '{}' created successfullly".format(user_post_saved.title)})