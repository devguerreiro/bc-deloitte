from django.db import models
from django.db.models.query import QuerySet

from gpapp.core.models.user import User


class StudentManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(profile=User.Profile.STUDENT)


class Student(User):
    objects = StudentManager()

    class Meta:
        proxy = True
