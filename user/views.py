from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from realEstateApp.models import Property
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class CurrentUserView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, property_id):  
        property_obj = get_object_or_404(Property, pk=property_id) 
        print(property_obj)
        user_profile = request.user.userprofile
        user_profile.favorites.add(property_obj)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        property_id = kwargs.get('property_id')
        property = get_object_or_404(Property, pk=property_id)
        user_profile = request.user.userprofile
        user_profile.favorites.remove(property)
        return Response(status=status.HTTP_204_NO_CONTENT)