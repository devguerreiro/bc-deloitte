import pytest

from gpapp.core.models.student import Student


@pytest.mark.django_db
class TestStudent:
    @staticmethod
    def test_should_be_able_to_list_students(client, populate_student):
        # given
        populate_student(3)

        url = "/api/v1/student/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert len(response.data) == 3

    @staticmethod
    def test_should_be_able_to_retrieve_an_student(client, populate_student):
        # given
        student = populate_student(1)[0]

        url = f"/api/v1/student/{student.id}/"

        # when
        response = client.get(url)

        # assert
        assert response.status_code == 200
        assert response.data["id"] == str(student.id)
        assert response.data["name"] == student.name
        assert response.data["email"] == student.email
        assert response.data["dob"] == student.dob.strftime("%d/%m/%Y")

    @staticmethod
    def test_should_be_able_to_delete_an_student(client, populate_student):
        # given
        student = populate_student(1)[0]

        url = f"/api/v1/student/{student.id}/"

        # when
        response = client.delete(url)

        # assert
        assert response.status_code == 204
        assert Student.objects.count() == 0

    @staticmethod
    def test_should_be_able_to_create_an_student(client, make_student):
        # given
        student = make_student()

        url = "/api/v1/student/"

        data = {
            "name": student.name,
            "email": student.email,
            "dob": student.dob.strftime("%d/%m/%Y"),
        }

        # when
        response = client.post(url, data)

        # assert
        assert response.status_code == 201
        assert Student.objects.count() == 1

    @staticmethod
    def test_should_be_able_to_update_an_student(client, populate_student):
        # given
        student = populate_student(1)[0]

        url = f"/api/v1/student/{student.id}/"

        data = {
            "name": "ze da manga",
            "email": "ze@damanga.com",
            "dob": "25/10/1980",
        }

        # when
        response = client.put(url, data, content_type="application/json")

        # assert
        assert response.status_code == 200

        student = Student.objects.get(pk=student.id)
        assert student.name == data["name"]
        assert student.email == data["email"]
        assert student.dob.strftime("%d/%m/%Y") == data["dob"]
