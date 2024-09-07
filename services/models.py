# models.py

from django.db import models
from django.conf import settings
from trail.models import Trail


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

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
