from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  
        fields = ["username", "email", "role", "profile_photo", "date_of_birth", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
