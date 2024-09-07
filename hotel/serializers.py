from rest_framework import serializers
from .models import Hotel, HotelImage, RoomType, Booking, BookingReview


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingReview
        fields = '__all__'
