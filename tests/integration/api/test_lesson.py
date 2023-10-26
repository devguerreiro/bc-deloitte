import pytest

from gpapp.core.models.lesson import Lesson, LessonGrade


@pytest.mark.django_db
class TestLesson:
    @staticmethod
    def test_should_be_able_to_list_lessons(client, populate_lesson):
        # given
        populate_lesson(3)

        url = "/api/v1/lesson/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

    @staticmethod
    def test_should_be_able_to_retrieve_an_lesson(client, populate_lesson):
        # given
        lesson = populate_lesson(1)[0]

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert response.data["id"] == str(lesson.id)
        assert response.data["name"] == lesson.name
        assert response.data["teachers_name"] == lesson.teachers_name
        assert response.data["load"] == lesson.load
        assert response.data["students"] == []

    @staticmethod
    def test_should_be_able_to_delete_an_lesson(client, populate_lesson):
        # given
        lesson = populate_lesson(1)[0]

        url = f"/api/v1/lesson/{lesson.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert Lesson.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_lesson(client, make_lesson):
        # given
        lesson = make_lesson()

        url = "/api/v1/lesson/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
            "load": lesson.load,
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201
        assert Lesson.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_create_an_lesson_with_students(
        client, make_lesson, populate_student
    ):
        # given
        student = populate_student(1)[0]
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
        response = client.post(url, data, content_type="application/json")

        # assert
        assert response.status_code == 201
        assert Lesson.objects.count() == 1
        assert LessonGrade.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_lesson(client, populate_lesson):
        # given
        lesson = populate_lesson(1)[0]

        url = f"/api/v1/lesson/{lesson.id}/"

        data = {
            "name": lesson.name,
            "teachers_name": lesson.teachers_name,
            "load": lesson.load,
        }

        # when
        response = client.put(url, data, content_type="application/json")

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert lesson.teachers_name == data["teachers_name"]
        assert lesson.load == data["load"]

    @staticmethod
    def test_should_be_able_to_update_an_lesson_with_students(
        client,
        populate_lesson,
        populate_student,
    ):
        # given
        student = populate_student(1)[0]
        lesson = populate_lesson(1)[0]

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
        response = client.put(url, data, content_type="application/json")

        # assert
        assert response.status_code == 200

        lesson = Lesson.objects.get(pk=lesson.id)
        assert lesson.name == data["name"]
        assert lesson.teachers_name == data["teachers_name"]
        assert lesson.load == data["load"]

        lesson_grade = lesson.lessongrade_set.first()
        assert lesson_grade.id == data["students"][0]["student"]
        assert lesson_grade.grades == data["students"][0]["grades"]
