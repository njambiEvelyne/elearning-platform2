from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import User
from .forms import CustomUserCreationForm

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Allow filtering users based on their role.
        Admins can view all users, while instructors and students see only themselves.
        """
        user = self.request.user
        if user.role == "admin":
            return User.objects.all()
        return User.objects.filter(id=user.id)


class CustomLoginView(LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(reverse("dashboard_redirect"))

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


def custom_logout(request):
    logout(request)
    return redirect("login")


class RegisterUserView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Account created successfully! You can now log in.")
        return super().form_valid(form)
    


@login_required
def dashboard_redirect(request):
    user = request.user

    if user.role == "admin":
        return redirect("users:admin_dashboard")
    elif user.role == "instructor":
        return redirect("users:instructor_dashboard")
    elif user.role == "student":
        return redirect("users:student_dashboard")
    else:
        return redirect("home")


@login_required
def admin_dashboard(request):
    return render(request, "users/admin_dashboard.html")


@login_required
def instructor_dashboard(request):
    return render(request, "users/instructor_dashboard.html")


@login_required
def student_dashboard(request):
    return render(request, "users/student_dashboard.html")
