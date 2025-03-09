from django.db import models

from django.contrib.auth.models import AbstractUser

"""
Creating the users of the platform
"""
class User(AbstractUser):
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('instructor', 'Instructor'),
    ('student', 'Student'),
  )
  role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='student')