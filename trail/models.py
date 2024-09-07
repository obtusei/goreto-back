from django.db import models
# Import User model from Django auth
from django.contrib.auth.models import User
from django.utils import timezone


class TravelMode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    difficulty = models.CharField(max_length=20)
    length = models.FloatField()
    duration = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50, blank=True, null=True)
    safety_info = models.TextField(blank=True, null=True)
    accessibility = models.TextField(blank=True, null=True)
    mode = models.ForeignKey(
        TravelMode, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Property {self.id}"


class Fact(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='facts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    # WALKING = 'Walking'
    # CYCLING = 'Cycling'
    # TRAVEL_MODE_CHOICES = [
    #     (WALKING, 'Walking'),
    #     (CYCLING, 'Cycling'),
    # ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    travel_mode = models.ForeignKey(
        TravelMode, on_delete=models.CASCADE,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Trail(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location_name = models.CharField(max_length=255, blank=True, null=True)
    review = models.ManyToManyField(Review, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # images = models.ImageField(upload_to='trails/', blank=True, null=True) #TODO: MAke multiple
    facts = models.ManyToManyField(Fact, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TrailImage(models.Model):
    trail = models.ForeignKey(
        Trail, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.trail.name}"


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    trails = models.ManyToManyField(Trail, blank=True)
    facts = models.ManyToManyField(Fact, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Coordinate(models.Model):
    STARTING = 'Starting'
    END = 'End'
    CHECKPOINT = 'CheckPoint'
    POINT_CHOICES = [
        (STARTING, 'Starting'),
        (END, 'End'),
        (CHECKPOINT, 'CheckPoint')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    point_name = models.CharField(
        max_length=20, choices=POINT_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, blank=True, null= True)

    def __str__(self):
        return self.name

