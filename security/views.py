# views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import RegisterSerializer

User = get_user_model()

# User Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
# Custom JWT login view for obtaining JWT token (if needed)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # Using default behavior from SimpleJWT

# Protected View Example
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': 'This is a protected route',
            'user': str(request.user),
            'role': request.user.role
        })


# views.py

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin

class AdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({
            'message': 'This is an admin-only route'
        })
