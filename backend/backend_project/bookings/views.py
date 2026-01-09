from rest_framework import generics
from .models import Car, Package, Booking
from .serializers import CarSerializer, PackageSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class PackageListAPIView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

def perform_create(self, serializer):
    booking = serializer.save(user=self.request.user)
    price = booking.days * 10000  # base price per day

    if booking.car_hours:
        price += booking.car_hours * 5000

    booking.total_price = price
    booking.save()
