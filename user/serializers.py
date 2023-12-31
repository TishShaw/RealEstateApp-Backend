from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from realEstateApp.serializers import PropertySerializer

class UserProfileSerializer(serializers.ModelSerializer):
    favorites = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['favorites']

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password", 'userprofile')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)

        return user
        
        