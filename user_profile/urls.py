from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, LanguageViewSet, CountryViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = router.urls
