from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from courses.models import Course
from .models import Enrollment
from .serializers import EnrollmentSerializer

from django.contrib.auth.decorators import login_required

from .forms import EnrollmentForm


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        Enrollment.objects.create(student=request.user, course=course) 
    
    if Enrollment.objects.filter(student=student, course=course).exists():
        messages.warning(request, "You are already enrolled in this course.")
        return redirect("users:student_dashboard")

    if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user  # Assign the logged-in user
            enrollment.course = course  # Assign the selected course
            enrollment.save()
            messages.success(request, "Enrollment successful!")
            return redirect("users:student_dashboard")  # Redirect to dashboard
    else:
        form = EnrollmentForm(initial={"email": request.user.email})

        else:
        Enrollment.objects.create(student=student, course=course)
        messages.success(request, "Successfully enrolled in the course!")


    return redirect("courses:course_detail", course_id=course.id)
   