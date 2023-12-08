from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User, UserFavorites

class UserCreateSerializer(UserCreateSerializer):
    favorite_properties = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'profile_photo', 'favorite_properties', )
        
class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorites
        fields = ('id', 'property', 'user', 'date', )