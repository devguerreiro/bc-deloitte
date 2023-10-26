import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from gpapp.core.models.coordinator import Coordinator
from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.models.student import Student
from gpapp.core.models.teacher import Teacher
from gpapp.core.models.user import User


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def admin_user():
    return baker.prepare(User, is_superuser=True)


@pytest.fixture()
def student_user():
    return baker.prepare(Student, profile=User.Profile.STUDENT)


@pytest.fixture()
def admin_client(client, admin_user):
    client.force_authenticate(admin_user)
    return client


@pytest.fixture()
def make_student():
    def factory(*args, **kwargs) -> Student:
        return baker.prepare(Student, profile=User.Profile.STUDENT, **kwargs)

    return factory


@pytest.fixture()
def make_teacher():
    def factory(*args, **kwargs) -> Teacher:
        return baker.prepare(Teacher, profile=User.Profile.TEACHER, **kwargs)

    return factory


@pytest.fixture()
def make_coordinator():
    def factory(*args, **kwargs) -> Coordinator:
        return baker.prepare(
            Coordinator,
            profile=User.Profile.COORDINATOR,
            **kwargs,
        )

    return factory


@pytest.fixture()
def make_lesson():
    def factory(*args, **kwargs) -> Lesson:
        return baker.prepare(Lesson, **kwargs)

    return factory


@pytest.fixture()
def make_lesson_grade():
    def factory(*args, **kwargs) -> LessonGrade:
        return baker.prepare(LessonGrade, **kwargs)

    return factory


@pytest.fixture()
def populate_student():
    def factory(*args, quantity: int = 1, **kwargs) -> Student:
        output = baker.make(
            Student,
            profile=User.Profile.STUDENT,
            _quantity=quantity,
            **kwargs,
        )
        return output if quantity > 1 else output[0]

    return factory


@pytest.fixture()
def populate_teacher():
    def factory(*args, quantity: int = 1, **kwargs) -> Teacher:
        output = baker.make(
            Teacher,
            profile=User.Profile.TEACHER,
            _quantity=quantity,
            **kwargs,
        )
        return output if quantity > 1 else output[0]

    return factory


@pytest.fixture()
def populate_coordinator():
    def factory(*args, quantity: int = 1, **kwargs) -> Coordinator:
        output = baker.make(
            Coordinator,
            profile=User.Profile.COORDINATOR,
            _quantity=quantity,
            **kwargs,
        )
        return output if quantity > 1 else output[0]

    return factory


@pytest.fixture()
def populate_lesson():
    def factory(*args, quantity: int = 1, **kwargs) -> Lesson:
        output = baker.make(Lesson, _quantity=quantity, **kwargs)
        return output if quantity > 1 else output[0]

    return factory


@pytest.fixture()
def populate_lesson_grade():
    def factory(*args, quantity: int = 1, **kwargs) -> Lesson:
        output = baker.make(LessonGrade, _quantity=quantity, **kwargs)
        return output if quantity > 1 else output[0]

    return factory
