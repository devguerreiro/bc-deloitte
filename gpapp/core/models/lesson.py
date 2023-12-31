from django.db import models

from gpapp.core.models.student import Student
from gpapp.core.models.teacher import Teacher


def get_default_grades():
    return [0, 0, 0, 0]


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
    grades = models.JSONField(default=get_default_grades)

    class Meta:
        verbose_name = "Disciplina Notas Aluno"
        verbose_name_plural = "Disciplinas Notas Alunos"
        unique_together = ["lesson", "student"]

    def __str__(self):
        return f"{self.lesson.name} - {self.student.name} | {self.grades}"

    def __repr__(self) -> str:
        return str(self)


class Lesson(models.Model):
    name = models.CharField(max_length=75, unique=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, related_name="lessons_as_teacher"
    )
    load = models.PositiveIntegerField()
    students = models.ManyToManyField(
        Student, through=LessonGrade, related_name="lessons_as_student"
    )

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return str(self)
