from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj == request.user
