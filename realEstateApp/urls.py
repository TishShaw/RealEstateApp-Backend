from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('properties/<slug:slug>/', PropertyDetail.as_view(), name='property-detail'),
]
