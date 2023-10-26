from rest_framework.permissions import BasePermission

from gpapp.core.models.user import User


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        return (
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

    def has_object_permission(self, request, view, obj):
        return request.user == obj
