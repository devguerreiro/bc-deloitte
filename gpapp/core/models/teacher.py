from django.db import models
from django.db.models.query import QuerySet

from gpapp.core.models.user import User


class TeacherManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(profile=User.Profile.TEACHER)


class Teacher(User):
    objects = TeacherManager()

    class Meta:
        proxy = True
