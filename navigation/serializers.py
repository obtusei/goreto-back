from rest_framework import serializers
from .models import UserNavigation

class UserNavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNavigation
        fields = '__all__'  # Or list the specific fields you need
