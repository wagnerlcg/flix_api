from rest_framework import permissions


class eleitorPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('vereadores.view_eleitor')

        if request.method == 'POST':
            return request.user.has_perm('vereadores.add_eleitor')

        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('vereadores.change_eleitor')

        if request.method == 'DELETE':
            return request.user.has_perm('vereadores.delete_eleitor')

        return False
