from rest_framework import permissions, generics
from .models import UserFavorites, User
from .serializers import UserFavoritesSerializer, UserCreateSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserFavoritesList(generics.ListCreateAPIView):
    queryset = UserFavorites.objects.all()
    serializer_class = UserFavoritesSerializer

class UserUserFavoritesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFavorites.objects.all()
    serializer_class = UserFavoritesSerializer

    permission_classes = [permissions.IsAuthenticated]
