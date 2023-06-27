# api/permissions.py

from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly


class IsAdministratorOwnerOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_superuser
                     or obj.author == request.user))
        )


class IsAdministratorOwnerOwnerNewsOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_superuser
                     or obj.author == request.user
                     or obj.news.author == request.user))
        )
