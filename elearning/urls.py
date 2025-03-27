"""
URL configuration for elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet,LessonViewSet
from enrollments.views import EnrollmentViewSet
from progress.views import ProgressViewSet
from quizzes.views import QuestionViewSet, SubmissionViewSet, QuizViewSet, AnswerViewSet
from users.views import UserViewset
from django.views.generic import TemplateView



router = DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'lessons', LessonViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'answer', AnswerViewSet)



urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  
    path("admin/", admin.site.urls),
    path('endpoints', include(router.urls)),
    path("users/", include('users.urls', namespace="users")),
    path('api-auth/', include('rest_framework.urls')),
    path("courses/", include('courses.urls'))  ,
    
]
