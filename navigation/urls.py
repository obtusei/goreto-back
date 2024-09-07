from rest_framework.routers import DefaultRouter
from .views import UserNavigationViewSet

router = DefaultRouter()
router.register(r'user-navigation', UserNavigationViewSet)

urlpatterns = router.urls
