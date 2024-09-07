from rest_framework import viewsets
from rest_framework.response import Response
from trail.models import Trail, Landmark
from trail.serializers import LandmarkSerializer
from .utils import haversine

class LandmarkRecommendationViewSet(viewsets.ViewSet):
    def list(self, request):
        trail_id = request.query_params.get('trail_id')
        if not trail_id:
            return Response({"error": "trail_id parameter is required"}, status=400)
        
        try:
            trail = Trail.objects.get(id=trail_id)
        except Trail.DoesNotExist:
            return Response({"error": "Trail not found"}, status=404)

        # Get the radius from query params, default to 1 km
        radius = request.query_params.get('radius', 1)
        try:
            radius = float(radius)
        except ValueError:
            return Response({"error": "Invalid radius value"}, status=400)

        landmarks = Landmark.objects.all()
        recommended_landmarks = []
        
        for landmark in landmarks:
            distance = haversine(trail.latitude, trail.longitude, landmark.latitude, landmark.longitude)
            if distance <= radius:
                recommended_landmarks.append(landmark)
        
        serializer = LandmarkSerializer(recommended_landmarks, many=True)
        return Response(serializer.data)
