from django.db import models
from django.db.models.query import QuerySet

from gpapp.core.models.user import User


class CoordinatorManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(profile=User.Profile.COORDINATOR)


class Coordinator(User):
    objects = CoordinatorManager()

    class Meta:
        proxy = True
