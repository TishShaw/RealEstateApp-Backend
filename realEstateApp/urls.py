from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
]
