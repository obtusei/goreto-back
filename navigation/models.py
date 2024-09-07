from django.db import models
from django.contrib.auth.models import User
from trail.models import Trail, Coordinate


class UserNavigation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    current_coordinate = models.ForeignKey(Coordinate, on_delete=models.CASCADE, related_name='current_navigation_set')
    last_checkpoint = models.ForeignKey(Coordinate, on_delete=models.SET_NULL, null=True, blank=True, related_name='last_navigation_set')
    completed_checkpoints = models.JSONField(default=list, blank=True)
    

    def __str__(self):
        return f"{self.user.username} navigating {self.trail.name}"
