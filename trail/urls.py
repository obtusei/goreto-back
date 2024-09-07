# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoordinateViewSet, TravelModeViewSet, PropertyViewSet, FactViewSet, ReviewViewSet, TrailViewSet, TrailImageViewSet, PlaceViewSet

router = DefaultRouter()
router.register(r'coordinates', CoordinateViewSet)
router.register(r'travelmodes', TravelModeViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'facts', FactViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'trails', TrailViewSet)
router.register(r'trailimages', TrailImageViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = router.urls
