from rest_framework import viewsets
from .models import Hotel, HotelImage, RoomType, Booking, BookingReview
from .serializers import HotelSerializer, HotelImageSerializer, RoomTypeSerializer, BookingSerializer, BookingReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingReviewViewSet(viewsets.ModelViewSet):
    queryset = BookingReview.objects.all()
    serializer_class = BookingReviewSerializer
    permission_classes = [IsAuthenticated]
