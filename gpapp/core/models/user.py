from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Profile(models.IntegerChoices):
        STUDENT = 0, "Estudante"
        TEACHER = 1, "Professor"
        COORDINATOR = 2, "Coordenador"
        ADMIN = 3, "Administrador"

    name = models.CharField(max_length=75)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    profile = models.IntegerField(
        choices=Profile.choices,
        default=Profile.STUDENT,
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name", "dob", "profile"]

    def __str__(self):
        return f"{self.profile} | {self.name} - {self.email}"

    def __repr__(self) -> str:
        return f"{self.profile} | {self.name} - {self.email}"
