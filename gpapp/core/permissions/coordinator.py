from rest_framework.permissions import BasePermission

from gpapp.core.models.user import User


class CoordinatorPermission(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.profile == User.Profile.COORDINATOR
            and view.basename in ["student", "teacher", "lesson"]
            and view.action != "student_grades"
        )

    def has_object_permission(self, request, _, __):
        return request.user and request.user.profile == User.Profile.COORDINATOR
