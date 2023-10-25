import pytest

from gpapp.core.models.teacher import Teacher


@pytest.mark.django_db
class TestTeacher:
    @staticmethod
    def test_should_be_able_to_list_teachers(client, populate_teacher):
        # given
        populate_teacher(3)

        url = "/api/v1/teacher/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

    @staticmethod
    def test_should_be_able_to_retrieve_an_teacher(client, populate_teacher):
        # given
        teacher = populate_teacher(1)[0]

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert response.data["id"] == str(teacher.id)
        assert response.data["name"] == teacher.name
        assert response.data["email"] == teacher.email
        assert response.data["dob"] == teacher.dob.strftime("%d/%m/%Y")

    @staticmethod
    def test_should_be_able_to_delete_an_teacher(client, populate_teacher):
        # given
        teacher = populate_teacher(1)[0]

        url = f"/api/v1/teacher/{teacher.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert Teacher.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_teacher(client, make_teacher):
        # given
        teacher = make_teacher()

        url = "/api/v1/teacher/"

        data = {
            "name": teacher.name,
            "email": teacher.email,
            "dob": teacher.dob.strftime("%d/%m/%Y"),
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201
        assert Teacher.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_teacher(client, populate_teacher):
        # given
        teacher = populate_teacher(1)[0]

        url = f"/api/v1/teacher/{teacher.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = client.put(url, data, content_type="application/json")

        # assert
        assert response.status_code == 200

        teacher = Teacher.objects.get(pk=teacher.id)
        assert teacher.name == data["name"]
        assert teacher.email == data["email"]
        assert teacher.dob.strftime("%d/%m/%Y") == data["dob"]
