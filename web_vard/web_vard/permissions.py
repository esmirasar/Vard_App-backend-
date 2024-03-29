from rest_framework import permissions


METHODS_USER = ['GET', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']
METHODS_FILE = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS']


class OnlyStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.user.is_staff else False


class UserPerCustom(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in METHODS_USER and request.user.is_authenticated:
            return True

        return False


class PerCustom(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in METHODS_FILE and request.user.is_authenticated:
            return True

        return False
