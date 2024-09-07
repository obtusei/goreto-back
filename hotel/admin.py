from django.contrib import admin
from .models import Hotel, HotelImage, RoomType, Booking, BookingReview


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1  # Number of empty forms for additional images


class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country', 'owner')  # Fields to display in the admin list view
    search_fields = ('name', 'city', 'state', 'owner__username')  # Search fields for quick lookup
    inlines = [HotelImageInline, RoomTypeInline]  # Show inline models in the hotel admin interface


@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image')  # Customize the list view for HotelImage
    search_fields = ('hotel__name',)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'capacity', 'price_per_night')
    search_fields = ('name', 'hotel__name')
    list_filter = ('hotel', 'capacity')  # Filter by hotel and capacity


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'room_type', 'check_in_date', 'check_out_date', 'status')
    search_fields = ('user__username', 'hotel__name', 'room_type__name')
    list_filter = ('status', 'check_in_date', 'check_out_date')  # Filters for easy sorting


@admin.register(BookingReview)
class BookingReviewAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'created_at')
    search_fields = ('booking__hotel__name', 'booking__user__username')
    list_filter = ('rating', 'created_at')
