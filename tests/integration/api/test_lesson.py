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
        assert response.data["teachers_name"] == lesson.teachers_name
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
    def test_should_be_able_to_create_an_lesson(admin_client, make_lesson):
        # given
        lesson = make_lesson()

        url = "/api/v1/lesson/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
            "load": lesson.load,
        }

        # when
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Lesson.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_create_an_lesson_with_students(
        admin_client, make_lesson, populate_student
    ):
        # given
        student = populate_student()
        lesson = make_lesson()

        url = "/api/v1/lesson/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
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
    def test_should_be_able_to_update_an_lesson(admin_client, populate_lesson):
        # given
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
            "load": lesson.load,
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert lesson.teachers_name == data["teachers_name"]
        assert lesson.load == data["load"]

    @staticmethod
    def test_should_be_able_to_update_an_lesson_with_students(
        admin_client,
        populate_lesson,
        populate_student,
    ):
        # given
        student = populate_student()
        lesson = populate_lesson()

        url = f"/api/v1/lesson/{lesson.id}/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
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
        assert lesson.teachers_name == data["teachers_name"]
        assert lesson.load == data["load"]

        lesson_grade = lesson.grades.first()
        assert lesson_grade.id == data["students"][0]["student"]
        assert lesson_grade.grades == data["students"][0]["grades"]
