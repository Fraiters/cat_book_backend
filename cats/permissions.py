from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdmin(BasePermission):
    """ Права доступа: 'Для владельца' или 'Для админа' """
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user or str(request.user) == "admin"
