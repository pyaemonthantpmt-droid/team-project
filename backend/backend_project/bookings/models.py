from django.db import models
from users.models import User
from destinations.models import Destination

class Car(models.Model):
    name = models.CharField(max_length=100)
    price_per_hour = models.IntegerField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name


class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    members = models.IntegerField()
    date = models.DateField()

    days = models.IntegerField(default=1)
    car_hours = models.IntegerField(default=0)

    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - Booking"

