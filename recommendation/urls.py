from rest_framework.routers import DefaultRouter
from .views import LandmarkRecommendationViewSet

router = DefaultRouter()

# Default Radius (1 km): /recommend-landmarks/?trail_id=1
# Custom Radius (e.g., 2 km): /recommend-landmarks/?trail_id=1&radius=2

router.register(r'recommend-landmarks', LandmarkRecommendationViewSet, basename='recommend-landmarks')

urlpatterns = router.urls
