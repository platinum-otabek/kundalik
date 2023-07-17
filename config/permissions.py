from rest_framework.permissions import BasePermission


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 't':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        print(2,request.user.roles)
        return True