from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, HotelImageViewSet, RoomTypeViewSet, BookingViewSet, BookingReviewViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'hotel-images', HotelImageViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'booking-reviews', BookingReviewViewSet)

urlpatterns = router.urls
