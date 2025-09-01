from django.db import models
from django.contrib.auth.models import User

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)  # e.g., Bike, Car
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username