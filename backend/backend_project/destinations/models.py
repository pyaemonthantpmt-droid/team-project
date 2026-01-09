from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.name
class Place(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places/')
    map_link = models.URLField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurants/')

    def __str__(self):
        return self.name


class Relaxation(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='relaxation/')

    def __str__(self):
        return self.name
