from rest_framework import viewsets
from .models import UserNavigation
from .serializers import UserNavigationSerializer

class UserNavigationViewSet(viewsets.ModelViewSet):
    queryset = UserNavigation.objects.all()
    serializer_class = UserNavigationSerializer
