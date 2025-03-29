from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["full_name", "email", "phone_number"]  # Fields to collect from student
