from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    """Пермишн для чтения, либо для админа"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated and request.user.role == 'admin')
        )


class ReviewAndComment(permissions.BasePermission):
    """Пермишн отзывов и комментариев"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == 'moderator'
            or request.user.role == 'admin'
            or obj.author == request.user
        )


class IsAdmin(permissions.BasePermission):
    """Пермишн для админа"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
