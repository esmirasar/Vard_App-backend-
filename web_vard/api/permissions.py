from rest_framework import permissions


MY_METHODS = ('GET', 'POST', 'PUT', 'HEAD', 'OPTIONS')


class ReadOnDeleteAd(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in MY_METHODS and request.user.is_authenticated:
            return True

        return request.user.is_authenticated and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        pass