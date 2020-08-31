from rest_framework import serializers
from django.contrib.auth.models import User
from .models import userProfile, UserPost


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = userProfile
        fields = '__all__'

class UserBriefSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserPostSerializer(serializers.ModelSerializer):
    User = UserBriefSerializer(read_only=True)

    class Meta:
        model = UserPost
        fields = "__all__"

    def create(self, validated_data):
        return UserPost.objects.create(**validated_data)
