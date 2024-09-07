
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger configuration
schema_view_swagger = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/trail/', include('trail.urls')),
    path('api/hotel/', include('hotel.urls')),
    path('api/users/', include('user_profile.urls')),
    path('docs/', schema_view),
    path('swagger<format>/', schema_view_swagger.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view_swagger.with_ui('swagger',
                                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_swagger.with_ui('redoc',
                                               cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
