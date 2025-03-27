from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import instructor_dashboard, add_course, CourseViewSet, LessonViewSet

router = DefaultRouter()

urlpatterns = [
    path('instructor/', instructor_dashboard, name='instructor_dashboard'),
    path('instructor/add/', add_course, name='add_course'),
    path('add/', add_course, name='add_course'),
    path('', include(router.urls)),  # Includes the auto-generated URLs


]
