import pytest

from gpapp.core.models.lesson import Lesson, LessonGrade


@pytest.mark.django_db
class TestLesson:
    @staticmethod
    def test_should_be_able_to_list_lessons(admin_client, populate_lesson):
        # given
        populate_lesson(quantity=3)

        url = "/api/v1/lesson/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert len(response.data) == 3

        assert response.data[0].get("id") is not None
        assert response.data[0].get("name") is not None
        assert response.data[0].get("teacher") is not None
        assert response.data[0].get("load") is not None
        assert response.data[0].get("students") is not None

    @staticmethod
    def test_should_be_able_to_retrieve_an_lesson(admin_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert response.data["id"] == lesson.id
        assert response.data["name"] == lesson.name
        assert response.data["teacher"]["id"] == lesson.teacher.id
        assert response.data["load"] == lesson.load
        assert response.data["students"] == []

    @staticmethod
    def test_should_be_able_to_delete_an_lesson(admin_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = admin_client.delete(url)

        # assert
        assert response.status_code == 204

        assert Lesson.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_lesson(
        admin_client, make_lesson, populate_teacher
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
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Lesson.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_create_an_lesson_with_students(
        admin_client, make_lesson, populate_student, populate_teacher
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
            "students": [
                {
                    "student": student.id,
                    "grades": [10, 8.5, 7, 9],
                }
            ],
        }

        # when
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Lesson.objects.count() == 1
        assert LessonGrade.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_lesson(
        admin_client, populate_lesson, populate_teacher
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
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert teacher.id == data["teacher"]
        assert lesson.load == data["load"]

    @staticmethod
    def test_should_be_able_to_update_an_lesson_with_students(
        admin_client, populate_lesson, populate_student, populate_teacher
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
            "students": [
                {
                    "student": student.id,
                    "grades": [10, 8.5, 7, 9],
                }
            ],
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert teacher.id == data["teacher"]
        assert lesson.load == data["load"]

        lesson_grade = lesson.grades.first()
        assert lesson_grade.id == data["students"][0]["student"]
        assert lesson_grade.grades == data["students"][0]["grades"]

    @staticmethod
    def test_should_be_able_to_update_the_student_grades(
        admin_client, populate_lesson_grade
    ):
        # given
        lesson_grade = populate_lesson_grade()

        url = f"/api/v1/lesson/{lesson_grade.lesson.id}/student_grades/"

        data = {
            "student": lesson_grade.student.id,
            "grades": [10, 10, 10, 10],
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        updated_lesson_grade = LessonGrade.objects.get(id=lesson_grade.id)
        assert updated_lesson_grade.grades == data["grades"]
