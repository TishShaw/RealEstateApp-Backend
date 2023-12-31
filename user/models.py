from django.db import models
from django.contrib.auth.models import User
from realEstateApp.models import Property

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Property, through='UserFavorites')
    
    def __str__(self):
        return f"{self.user.username}"

class UserFavorites(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True) 
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.property.title} favorited by {self.user_profile.user.username}"
