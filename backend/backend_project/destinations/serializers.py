from rest_framework import serializers
from .models import Destination, Place, Restaurant, Relaxation

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RelaxationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relaxation
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'
