# models.py
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.response import Response
from trail.models import Trail
from recommendation.utils import haversine
from services.utils import send_email


class Alert(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    problem = models.TextField()
    trail = models.ForeignKey(
        Trail, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alert by {self.user} at [ Lat = {self.latitude} Lon= {self.longitude}  regarding {self.problem}"


class LocalAuthority(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()


@receiver(pre_save, sender=Alert)
def alert_pre_save(sender, instance, **kwargs):
    # Convert latitude and longitude to float
    alert_lat = float(instance.latitude)
    alert_lon = float(instance.longitude)

    # Find the nearest LocalAuthority
    nearest_authority = None
    min_distance = float('inf')

    for authority in LocalAuthority.objects.all():
        authority_lat = float(authority.latitude)
        authority_lon = float(authority.longitude)
        distance = haversine(alert_lat, alert_lon,
                             authority_lat, authority_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_authority = authority

    # Send an email if a nearest authority is found
    if nearest_authority:
        result = send_email(nearest_authority.email, instance)
        if result['isSuccess']:
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
