# views.py

from rest_framework import viewsets
from .models import Coordinate, TravelMode, Property, Fact, Review, Trail, TrailImage, Place
from .serializers import CoordinateSerializer, TravelModeSerializer, PropertySerializer, FactSerializer, ReviewSerializer, TrailSerializer, TrailImageSerializer, PlaceSerializer


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


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
