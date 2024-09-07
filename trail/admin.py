from django.contrib import admin
from .models import (
    Coordinate, TravelMode, Property, Fact, Review, Trail, TrailImage, Place
)


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lon', 'point_name')
    search_fields = ('name', 'lat', 'lon')
    list_filter = ('point_name',)
    ordering = ('name',)


class TravelModeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('difficulty', 'length', 'duration',
                    'temperature', 'safety_info', 'accessibility')
    search_fields = ('difficulty', 'duration')
    list_filter = ('difficulty',)
    ordering = ('difficulty', 'length')


class FactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    ordering = ('title',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'reviewer', 'property', 'travel_mode')
    search_fields = ('title', 'reviewer__username', 'property__id')
    list_filter = ('travel_mode', 'property')
    ordering = ('-id',)


class TrailImageInline(admin.TabularInline):
    model = TrailImage
    extra = 1


class TrailAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location_name', 'creator')
    search_fields = ('name', 'description', 'location_name')
    list_filter = ('creator',)
    ordering = ('name',)
    inlines = [TrailImageInline]


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)


# Register the models with their corresponding admin classes
admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(TravelMode, TravelModeAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Trail, TrailAdmin)
# TrailImage is registered directly as it is managed through inlines
admin.site.register(TrailImage)
admin.site.register(Place, PlaceAdmin)
