import pytest

from gpapp.core.models.teacher import Teacher
from gpapp.core.models.user import User


@pytest.mark.django_db
class TestTeacher:
    @staticmethod
    def test_should_be_able_to_list_teachers(admin_client, populate_teacher):
        # given
        populate_teacher(quantity=3)

        url = "/api/v1/teacher/"

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
    def test_should_be_able_to_retrieve_an_teacher(admin_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = admin_client.get(url)

        # assert
        assert response.status_code == 200

        assert response.data["id"] == teacher.id
        assert response.data["name"] == teacher.name
        assert response.data["email"] == teacher.email
        assert response.data["dob"] == teacher.dob.strftime("%d/%m/%Y")
        assert response.data["profile"] == User.Profile.TEACHER
        assert response.data.get("password") is None

    @staticmethod
    def test_should_be_able_to_delete_an_teacher(admin_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = admin_client.delete(url)

        # assert
        assert response.status_code == 204

        assert Teacher.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_teacher(admin_client, make_teacher):
        # given
        teacher = make_teacher()

        url = "/api/v1/teacher/"

        data = {
            "name": teacher.name,
            "email": teacher.email,
            "password": teacher.password,
            "dob": teacher.dob.strftime("%d/%m/%Y"),
            "profile": User.Profile.TEACHER,
        }

        # when
        response = admin_client.post(url, data)

        # assert
        assert response.status_code == 201

        assert Teacher.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_teacher(admin_client, populate_teacher):
        # given
        teacher = populate_teacher()

        url = f"/api/v1/teacher/{teacher.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = admin_client.put(url, data)

        # assert
        assert response.status_code == 200

        teacher = Teacher.objects.get(pk=teacher.id)
        assert teacher.name == data["name"]
        assert teacher.email == data["email"]
        assert teacher.dob.strftime("%d/%m/%Y") == data["dob"]
