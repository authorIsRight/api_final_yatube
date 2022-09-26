from rest_framework import permissions


# оставил только один пермишн, изменил в settings на IsAuthenticatedOrReadOnly
class IsAuthOrAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
