from rest_framework import serializers
from .models import Property, PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ("id", "image", "property")

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Property
        fields = ('id', 'title', 'slug', 'type', 'description', 'price', 'num_of_bedrooms', 'num_of_bathrooms', 'sqft', 'address', 'city', 'state', 'zip_code', 'amenities', 'listing_status', 'date_added', 'images')
