from rest_framework import permissions


class CanBeTaken(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.can_be_taken(request.user)
