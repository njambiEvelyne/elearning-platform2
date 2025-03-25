from django.urls import path
from .views import instructor_dashboard, add_course

urlpatterns = [
    path('instructor/', instructor_dashboard, name='instructor_dashboard'),
    path('instructor/add/', add_course, name='add_course'),
]
