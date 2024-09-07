from django.db import models
from django.contrib.auth.models import User
from django.core.files.images import ImageFile


class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    SUBSCRIPTION_TYPES = [
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
    ]

    type = models.CharField(
        max_length=10, choices=SUBSCRIPTION_TYPES, unique=True)
    discount = models.FloatField()

    def __str__(self):
        return self.type


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    citizenship = models.ImageField(
        upload_to='citizenships/', blank=True, null=True)
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    reward_point = models.FloatField(default=0.0)
    subscription_model = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
