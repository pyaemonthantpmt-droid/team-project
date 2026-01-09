from django.urls import path
from .views import CarListAPIView, PackageListAPIView, BookingCreateAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('packages/', PackageListAPIView.as_view()),
    path('book/', BookingCreateAPIView.as_view()),
]
