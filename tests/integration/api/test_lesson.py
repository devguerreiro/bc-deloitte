import pytest

from gpapp.core.models.lesson import Lesson, LessonGrade


@pytest.mark.django_db
class TestLesson:
    @staticmethod
    def test_should_be_able_to_list_lessons(staff_client, populate_lesson):
        # given
        populate_lesson(quantity=3)

        url = "/api/v1/lesson/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

        assert len(response.data) == 3

        assert response.data[0].get("id") is not None
        assert response.data[0].get("name") is not None
        assert response.data[0].get("teacher") is not None
        assert response.data[0].get("load") is not None
        assert response.data[0].get("students") is not None

    @staticmethod
    def test_should_be_able_to_retrieve_an_lesson(staff_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = staff_client.get(url)

        # assert
        assert response.status_code == 200

        assert response.data["id"] == lesson.id
        assert response.data["name"] == lesson.name
        assert response.data["teacher"]["id"] == lesson.teacher.id
        assert response.data["load"] == lesson.load
        assert response.data["students"] == []

    @staticmethod
    def test_should_be_able_to_delete_an_lesson(staff_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = staff_client.delete(url)

        # assert
        assert response.status_code == 204

        assert Lesson.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_lesson(
        staff_client, make_lesson, populate_teacher
    ):
        # given
        lesson = make_lesson()
        teacher = populate_teacher()

        url = "/api/v1/lesson/"

        data = {
            "name": lesson.name,
            "teacher": teacher.id,
            "load": lesson.load,
        }

        # when
        response = staff_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Lesson.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_create_an_lesson_with_students(
        staff_client, make_lesson, populate_student, populate_teacher
    ):
        # given
        student = populate_student()
        teacher = populate_teacher()
        lesson = make_lesson()

        url = "/api/v1/lesson/"

        data = {
            "name": lesson.name,
            "teacher": teacher.id,
            "load": lesson.load,
            "students": [student.id],
        }

        # when
        response = staff_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Lesson.objects.count() == 1
        assert LessonGrade.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_lesson(
        staff_client, populate_lesson, populate_teacher
    ):
        # given
        lesson = populate_lesson()
        teacher = populate_teacher()

        url = f"/api/v1/lesson/{lesson.id}/"

        data = {
            "name": lesson.name,
            "teacher": teacher.id,
            "load": lesson.load,
        }

        # when
        response = staff_client.put(url, data)

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert teacher.id == data["teacher"]
        assert lesson.load == data["load"]

    @staticmethod
    def test_should_be_able_to_update_an_lesson_with_students(
        staff_client, populate_lesson, populate_student, populate_teacher
    ):
        # given
        student = populate_student()
        lesson = populate_lesson()
        teacher = populate_teacher()

        url = f"/api/v1/lesson/{lesson.id}/"

        data = {
            "name": lesson.name,
            "teacher": teacher.id,
            "load": lesson.load,
            "students": [student.id],
        }

        # when
        response = staff_client.put(url, data)

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert teacher.id == data["teacher"]
        assert lesson.load == data["load"]

        lesson_grade = lesson.grades.first()
        assert lesson_grade.student.id == data["students"][0]

    @staticmethod
    def test_should_be_able_to_update_the_student_grades(
        staff_client, populate_lesson_grade, populate_lesson
    ):
        # given
        lesson = populate_lesson()
        lesson_grade = populate_lesson_grade(lesson=lesson, quantity=2)

        url = f"/api/v1/lesson/{lesson_grade[1].lesson.id}/student_grades/"

        data = {
            "student": lesson_grade[1].student.id,
            "grades": [10, 10, 10, 10],
        }

        # when
        response = staff_client.put(url, data)

        # assert
        assert response.status_code == 200

        updated_lesson_grade = LessonGrade.objects.get(id=lesson_grade[1].id)
        assert updated_lesson_grade.grades == data["grades"]
