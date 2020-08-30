from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile, UserPost
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, UserPostSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


class userProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class userProfileView(APIView):
    def get(self, request):
        accounts = userProfile.objects.all()
        serializer = userProfileSerializer()
        return Response({"userProfile": serializer.data})

class userProfileDetailListView(RetrieveUpdateDestroyAPIView):
    queryset =  userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

class UserPostView(APIView):
    def post(self):
        user_post = request.data.get('user_post')
        serializer = UserPostSerializer(data=user_post)
        if serializer.is_valid(raise_exception=True):
            user_post_saved = serializer.save()
        return Response({'success': "Post '{}' created successfullly".format(user_post_saved.title)})