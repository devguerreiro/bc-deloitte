from rest_framework.permissions import BasePermission

from gpapp.core.models.user import User


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (
            request.user
            and request.user.profile == User.Profile.STUDENT
            and view.basename == "student"
            and view.action
            in [
                "retrieve",
                "update",
                "grades",
            ]
        )

    def has_object_permission(self, request, _, obj):
        return request.user.is_superuser or request.user == obj
