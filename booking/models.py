from django.db import models
from realEstateApp.models import Property
from django.contrib.auth import get_user_model
User = get_user_model()

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    message = models.TextField( null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.property.title + ' - ' + self.user.email