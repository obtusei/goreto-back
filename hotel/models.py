from django.db import models
from django.contrib.auth.models import User
from trail.models import Coordinate
from django.utils import timezone


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Owner of the hotel
    coordinate =  models.ForeignKey(Coordinate,  on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.hotel.name}"


class RoomType(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Number of people the room can accommodate
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    # Possible values: Pending, Confirmed, Cancelled
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user.username} at {self.hotel.name}"


class BookingReview(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # e.g., 1 to 5 stars
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for Booking {self.booking.id}"
