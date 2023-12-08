from django.urls import path, include
from .views import UserFavoritesList, UsersList

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('api/users/', UsersList.as_view(), name='users_list'),
    path('api/user/favorites', UserFavoritesList.as_view(), name='user_favorites_list')
]