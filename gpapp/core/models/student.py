from typing import Any

from django.contrib.auth.models import UserManager
from django.db.models.query import QuerySet

from gpapp.core.models.user import User


class StudentManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(profile=User.Profile.STUDENT)

    def create_user(
        self,
        username: str,
        email: str | None = ...,
        password: str | None = ...,
        **extra_fields: Any
    ) -> Any:
        return super().create_user(
            username, email, password, **extra_fields, profile=User.Profile.STUDENT
        )


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True
