from django.db import models


class Coordinator(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField(unique=True)
    dob = models.DateField()

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)
