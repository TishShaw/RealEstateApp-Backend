# In your models.py or a dedicated file where you customize Django's auth models
from django.db import models
from realEstateApp.models import Property

class User(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)
    username = models.CharField(verbose_name='username', max_length=255, unique=True)
    password = models.CharField(verbose_name='password', max_length=255)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    profile_photo = models.ImageField(upload_to='images', null=True, blank=True)
    favorite_properties = models.ManyToManyField(Property, related_name='custom_user_favorite_properties')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserFavorites(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='custom_user_favorite_property')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.property.title} - {self.user.email}"
