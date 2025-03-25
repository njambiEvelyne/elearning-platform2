from typing import Generic
from django.forms import ValidationError
from rest_framework import viewsets
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView
from users import custom_permissions
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet): 
    """
    ViewSet for user management (CRUD)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserListView(ListAPIView):
    """Retrieve all users (Admin only)"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDetailView(RetrieveUpdateAPIView):
    """Retrieve or update a specific user (User can edit 
    only their data)"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id) 

class RegisterUserView(generics.CreateAPIView):
    """Allows new users to register"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise ValidationError({"password": e.messages})
        user = serializer.save()
        return user
    
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class LoginView(TokenObtainPairView):
    """Login view that returns access and refresh tokens"""
    permission_classes = [AllowAny]

from  users.custom_permissions import IsAdminUser 

class SomeAdminView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
