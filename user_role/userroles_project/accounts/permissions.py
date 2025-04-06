from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrModeratorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods = GET
        if request.method in SAFE_METHODS:
            return True

        # Owner
        if obj == request.user:
            return True

        # Moderator can edit/delete users
        if request.user.role == 'moderator' and obj.role == 'user':
            return True

        # Admin can edit/delete anyone
        if request.user.role == 'admin':
            return True

        return False
