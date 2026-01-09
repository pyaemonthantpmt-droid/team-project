from rest_framework import generics
from .models import Destination, Place, Restaurant, Relaxation
from .serializers import (
    DestinationSerializer,
    PlaceSerializer,
    RestaurantSerializer,
    RelaxationSerializer
)

class DestinationListAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class PlaceListAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        destination_id = self.kwargs['destination_id']
        return Place.objects.filter(destination_id=destination_id)


class RestaurantListAPIView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        destination_id = self.kwargs['destination_id']
        return Restaurant.objects.filter(destination_id=destination_id)


class RelaxationListAPIView(generics.ListAPIView):
    serializer_class = RelaxationSerializer

    def get_queryset(self):
        destination_id = self.kwargs['destination_id']
        return Relaxation.objects.filter(destination_id=destination_id)
