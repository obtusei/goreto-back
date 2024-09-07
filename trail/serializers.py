from rest_framework import serializers
from .models import Coordinate, TravelMode, Property, Fact, Review, Trail, TrailImage, Place, Landmark


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = '__all__'


class TravelModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelMode
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TrailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailImage
        fields = '__all__'


class TrailSerializer(serializers.ModelSerializer):
    images = TrailImageSerializer(many=True, read_only=True)

    class Meta:
        model = Trail
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    trails = TrailSerializer(many=True, read_only=True)
    facts = FactSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


# Landmark Serializer
class LandmarkSerializer(serializers.ModelSerializer):
    trail = TrailSerializer(read_only=True)  # Nested Trail serializer for read-only
    coordinate = CoordinateSerializer(read_only=True)  # Nested Coordinate serializer for read-only

    class Meta:
        model = Landmark
        fields = ['id', 'name', 'trail', 'coordinate', 'image', 'created_at', 'last_modified']
