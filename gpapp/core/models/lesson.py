from django.db import models

from gpapp.core.models.student import Student


class LessonGrade(models.Model):
    lesson = models.ForeignKey(
        "Lesson",
        on_delete=models.PROTECT,
        related_name="grades",
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name="grades",
    )
    grades = models.JSONField(default=list)

    class Meta:
        unique_together = ["lesson", "student"]

    def __str__(self):
        return f"{self.lesson.name} - {self.student.name} | {self.grades}"

    def __repr__(self) -> str:
        return str(self)


class Lesson(models.Model):
    name = models.CharField(max_length=75, unique=True)
    teachers_name = models.CharField(max_length=75)
    load = models.PositiveIntegerField()
    students = models.ManyToManyField(
        Student, through=LessonGrade, related_name="lessons"
    )

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)
