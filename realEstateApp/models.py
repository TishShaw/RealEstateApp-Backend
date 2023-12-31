from django.db import models
class Property(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(blank=True, unique=True)
    type=models.CharField(max_length=100, default='', null=True)
    description = models.TextField(null=True, blank=True, default='', max_length=5000)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    num_of_bedrooms = models.DecimalField(null=True, max_digits=5, decimal_places=2, default=0)
    num_of_bathrooms = models.DecimalField(null=True, max_digits=5, decimal_places=2, default=0)
    sqft = models.IntegerField(null=True, default=0)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip_code = models.IntegerField(null=True)
    amenities = models.CharField(max_length=255, null=True)
    listing_status = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
        
    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')
   
class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name 

    
