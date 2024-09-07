# myapp/urls.py

from django.urls import path
from .views import HelloWorld, RegisterView, LoginView, LogoutView, SessionCheckView


urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('session-check/', SessionCheckView.as_view(), name='session-check'),
]
