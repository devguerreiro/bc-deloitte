import pytest
from model_bakery import baker

from gpapp.core.models.coordinator import Coordinator
from gpapp.core.models.lesson import Lesson, LessonGrade
from gpapp.core.models.student import Student
from gpapp.core.models.teacher import Teacher


@pytest.fixture()
def make_student():
    def factory(*args, **kwargs) -> Student:
        return baker.prepare(Student, **kwargs)

    return factory


@pytest.fixture()
def make_teacher():
    def factory(*args, **kwargs) -> Teacher:
        return baker.prepare(Teacher, **kwargs)

    return factory


@pytest.fixture()
def make_coordinator():
    def factory(*args, **kwargs) -> Coordinator:
        return baker.prepare(Coordinator, **kwargs)

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
    def factory(quantity: int, *args, **kwargs) -> Student:
        return baker.make(Student, **kwargs, _quantity=quantity)

    return factory


@pytest.fixture()
def populate_teacher():
    def factory(quantity: int, *args, **kwargs) -> Teacher:
        return baker.make(Teacher, **kwargs, _quantity=quantity)

    return factory


@pytest.fixture()
def populate_coordinator():
    def factory(quantity: int, *args, **kwargs) -> Coordinator:
        return baker.make(Coordinator, **kwargs, _quantity=quantity)

    return factory
