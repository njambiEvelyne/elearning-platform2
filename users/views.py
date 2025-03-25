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
from .serializers import LoginView, UserSerializer
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

from django.shortcuts import redirect
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = "users/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        extra_info = form.cleaned_data.get("extra_info")
        # Process extra_info (e.g., save to session or log it)
        self.request.session["extra_info"] = extra_info
        return response

from  users.custom_permissions import IsAdminUser 

class SomeAdminView(generics.ListAPIView):
    permission_classes = [IsAdminUser]


from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class UserLoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access this view

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)



from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
@api_view(["POST"])
@permission_classes([AllowAny])  # Allow anyone to login
def login_view(request):
    return Response({"message": "Login successful"})