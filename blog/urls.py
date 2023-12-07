from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('blog/', BlogList.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]
