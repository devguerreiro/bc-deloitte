from rest_framework.permissions import BasePermission

from gpapp.core.models.lesson import Lesson
from gpapp.core.models.teacher import Teacher
from gpapp.core.models.user import User


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and (
            request.user.is_superuser
            or request.user.profile != User.Profile.TEACHER
            or (
                request.user.profile == User.Profile.TEACHER
                and (
                    view.basename == "lesson"
                    and view.action in ["list", "retrieve", "student_grades"]
                    or view.basename == "teacher"
                    and view.action == "retrieve"
                )
            )
        )

    def has_object_permission(self, request, _, obj):
        return request.user and (
            request.user.is_superuser
            or request.user.profile != User.Profile.TEACHER
            or (
                request.user.profile == User.Profile.TEACHER
                and (
                    (isinstance(obj, Lesson) and obj.teacher == request.user)
                    or (isinstance(obj, Teacher) and obj == request.user)
                )
            )
        )
