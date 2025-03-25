from typing import Generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView
from users import permissions
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
