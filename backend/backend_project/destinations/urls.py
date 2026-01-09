from django.urls import path
from .views import (
    DestinationListAPIView,
    PlaceListAPIView,
    RestaurantListAPIView,
    RelaxationListAPIView
)

urlpatterns = [
    path('', DestinationListAPIView.as_view()),
    path('<int:destination_id>/places/', PlaceListAPIView.as_view()),
    path('<int:destination_id>/restaurants/', RestaurantListAPIView.as_view()),
    path('<int:destination_id>/relaxation/', RelaxationListAPIView.as_view()),
]
