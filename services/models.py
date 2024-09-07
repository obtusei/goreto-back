# # models.py

# from django.db import models
# from django.conf import settings
# from trail.models import Coordinate, Trail


# class Alert(models.Model):
#     coordinate = models.ForeignKey(Coordinate, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     problem = models.TextField()
#     trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Alert by {self.user} at [ Lat = {self.coordinate.lat} Lon= {self.coordinate.lon}  regarding {self.problem}"
