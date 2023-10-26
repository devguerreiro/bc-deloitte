from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class ProfileChoices(models.IntegerChoices):
        STUDENT = 0, "Estudante"
        TEACHER = 1, "Teacher"
        COORDINATOR = 2, "Coordenador"

    profile = models.IntegerField(
        choices=ProfileChoices.choices, default=ProfileChoices.STUDENT
    )
