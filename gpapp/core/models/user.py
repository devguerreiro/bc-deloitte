from typing import Any

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields: Any) -> Any:
        return super().create_user(email, email, password, **extra_fields)

    def create_superuser(
        self, email: str, password: str, **extra_fields: Any
    ) -> "User":
        return super().create_superuser(email, email, password, **extra_fields)


class User(AbstractUser):
    class Profile(models.IntegerChoices):
        STUDENT = 0, "Estudante"
        TEACHER = 1, "Professor"
        COORDINATOR = 2, "Coordenador"

    name = models.CharField(max_length=75)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    profile = models.IntegerField(
        choices=Profile.choices,
        default=Profile.STUDENT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.profile} | {self.name} - {self.email}"

    def __repr__(self) -> str:
        return f"{self.profile} | {self.name} - {self.email}"
