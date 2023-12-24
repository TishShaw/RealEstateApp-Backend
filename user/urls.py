from django.urls import path
from .views import UserCreate, CurrentUserView, AddFavoriteView, RemoveFavoriteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'), 
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_view"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh_view"),
    path('api/user/', CurrentUserView.as_view(), name='current_user'),
    path('api/user/add-favorite/<int:property_id>/', AddFavoriteView.as_view(), name='add_favorite'),
    path('api/user/remove-favorite/<int:property_id>/', RemoveFavoriteView.as_view(), name='remove_favorite'),
]
