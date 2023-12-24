from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import AllowAny
class PropertyList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer