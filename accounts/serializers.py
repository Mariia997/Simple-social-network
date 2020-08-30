from rest_framework import serializers
from .models import userProfile, UserPost


class userProfileBriefSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'

class UserPostSerializer(serializers.ModelSerializer):
    userProfile = userProfileBriefSerializer(read_only=True)

    class Meta:
        model = UserPost
        fields = "__all__"

    def create(self, validated_data):
        return UserPost.objects.create(**validated_data)
