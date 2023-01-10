from rest_framework.permissions import (
    SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly
)

from reviews.models import User


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_superuser
        )


class IsStaffOrAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in SAFE_METHODS
            or request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_authenticated
            and request.user.role == User.MODERATOR
        )


class MePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, view, request, obj):
        return request.method in ('PATCH', 'GET')


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_staff
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return request.method in ('GET', 'POST', 'PATCH', 'DELETE')
