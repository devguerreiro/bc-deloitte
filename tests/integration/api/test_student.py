import pytest

from gpapp.core.models.student import Student
from gpapp.core.models.user import User


@pytest.mark.django_db
class TestStudent:
    @staticmethod
    def test_should_be_able_to_list_students(admin_client, populate_student):
        # given
        populate_student(quantity=3)

        url = "/api/v1/student/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert len(response.data) == 3

        assert response.data[0].get("id") is not None
        assert response.data[0].get("name") is not None
        assert response.data[0].get("email") is not None
        assert response.data[0].get("dob") is not None
        assert response.data[0].get("profile") is not None
        assert response.data[0].get("password") is None

    @staticmethod
    def test_should_be_able_to_retrieve_an_student(
        admin_client,
        populate_student,
    ):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert response.data["id"] == student.id
        assert response.data["name"] == student.name
        assert response.data["email"] == student.email
        assert response.data["dob"] == student.dob.strftime("%d/%m/%Y")
        assert response.data["profile"] == User.Profile.STUDENT
        assert response.data.get("password") is None

    @staticmethod
    def test_should_be_able_to_delete_an_student(admin_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        # when
        response = admin_client.delete(url)

        # assert
        assert response.status_code == 204

        assert Student.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_student(admin_client, make_student):
        # given
        student = make_student()

        url = "/api/v1/student/"

        data = {
            "name": student.name,
            "email": student.email,
            "password": student.password,
            "dob": student.dob.strftime("%d/%m/%Y"),
            "profile": User.Profile.STUDENT,
        }

        # when
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Student.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_student(admin_client, populate_student):
        # given
        student = populate_student()

        url = f"/api/v1/student/{student.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        student = Student.objects.get(pk=student.id)
        assert student.name == data["name"]
        assert student.email == data["email"]
        assert student.dob.strftime("%d/%m/%Y") == data["dob"]

    @staticmethod
    def test_should_be_able_to_get_your_grades(
        client, populate_student, populate_lesson_grade
    ):
        # given
        student = populate_student()

        populate_lesson_grade(student=student, quantity=5)

        url = f"/api/v1/student/{student.id}/grades/"

        client.force_authenticate(student)

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200

        assert len(response.data) == 5

        assert response.data[0].get("id") is not None
        assert response.data[0].get("lesson") is not None
        assert response.data[0].get("grades") is not None
