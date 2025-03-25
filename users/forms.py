from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    extra_info = forms.CharField(max_length=100, required=False, help_text="Enter additional details")

