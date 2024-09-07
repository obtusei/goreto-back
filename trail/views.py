from rest_framework import viewsets
from .models import Coordinate, TravelMode, Property, Fact, Review, Trail, TrailImage, Place, Landmark
from .serializers import (CoordinateSerializer, TravelModeSerializer, PropertySerializer, 
                          FactSerializer, ReviewSerializer, TrailSerializer, 
                          TrailImageSerializer, PlaceSerializer, LandmarkSerializer)


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


class TravelModeViewSet(viewsets.ModelViewSet):
    queryset = TravelMode.objects.all()
    serializer_class = TravelModeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class FactViewSet(viewsets.ModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TrailImageViewSet(viewsets.ModelViewSet):
    queryset = TrailImage.objects.all()
    serializer_class = TrailImageSerializer


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

    def get_queryset(self):
        """Override to allow query parameters for filtering the number of latest trails by the creation date."""
        queryset = super().get_queryset().order_by('-last_modified')  # Order by latest created_at date
        limit = self.request.query_params.get('limit', 5)  # Get the 'limit' query param (default is 5)
        if limit is not None:
            try:
                limit = int(limit)
                queryset = queryset[:limit]  # Return only the number of trails specified by 'limit'
            except ValueError:
                pass  # If the limit is not a valid integer, return all trails
        return queryset


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


# Landmark ViewSet
class LandmarkViewSet(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
