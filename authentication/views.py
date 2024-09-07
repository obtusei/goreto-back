from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.middleware.csrf import get_token  # Import get_token

from services.utils import send_email
from services.models import Alert


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            user = form.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in, creating a session

            # Get session key
            session_key = request.session.session_key

            # Get CSRF token
            csrf_token = get_token(request)  # Use get_token to retrieve CSRF token

            # Prepare user data
            user_data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }

            # Return session key, CSRF token, and user information
            return Response(
                {
                    "message": "Logged in successfully",
                    "session_key": session_key,
                    "csrf_token": csrf_token,
                    "user_info": user_data
                },
                status=status.HTTP_200_OK
            )

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class HelloWorld(APIView):
    def get(self, request):
        alert = Alert.objects.get(pk=1)
        result = send_email('ng4111894@gmail.com', alert)
        return Response({'result': result}, status=status.HTTP_200_OK)
        if request.user.is_authenticated:
            return Response({"message": f"Hello, {request.user.username}"}, status=status.HTTP_200_OK)
        return Response({"message": "Hello, World"}, status=status.HTTP_200_OK)


class SessionCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return Response({'isLogout': True}, status=status.HTTP_200_OK)
        return Response({'isLogout': False}, status=status.HTTP_200_OK)
