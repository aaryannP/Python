from rest_framework import permissions

class IsPremiumUser(permissions.BasePermission):
    """
    Custom permission to only allow premium users to access the API.
    """
    def has_permission(self, request, view):
        # Allow access only if user is authenticated and has a profile with is_premium=True
        if not request.user or not request.user.is_authenticated:
            return False
            
        return hasattr(request.user, 'profile') and request.user.profile.is_premium
