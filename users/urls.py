from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.serializers import LoginView
from rest_framework.authtoken.views import obtain_auth_token

from .views import CustomLoginView, UserListView, UserDetailView, RegisterUserView  
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    #path('login/', CustomLoginView.as_view(), name='login'),  # Use CustomLoginView for login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # Django login form

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

]
