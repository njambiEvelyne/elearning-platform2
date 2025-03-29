from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets

from courses.models import Course
from .models import Enrollment
from .serializers import EnrollmentSerializer

from django.contrib.auth.decorators import login_required


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        Enrollment.objects.create(student=request.user, course=course)  

    return redirect('student_dashboard')  # 🔄 Redirect back to dashboard