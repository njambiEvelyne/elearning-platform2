from rest_framework import permissions

class IsAdminOrInstructorOrReadOnly(permissions.BasePermission):
    """
    - Admins have full access.
    - Instructors can create, update, and delete courses and lessons.
    - Students can only view (read-only).
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS for all users (read-only access)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow full access to admins
        if request.user.is_authenticated and request.user.is_staff:
            return True
        # Allow modification for instructors only
        return request.user.is_authenticated and request.user.role == "instructor"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Admins can modify anything
        if request.user.is_authenticated and request.user.is_staff:
            return True
        # Instructors can only modify their own courses/lessons
        return request.user.is_authenticated and request.user.role == "instructor"
